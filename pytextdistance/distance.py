import functools
import multiprocessing
import os
import unicodedata

from pytextdistance.outputfile import ExcelHandler, CsvHandler, TextFileHandler


class FileTypeError(Exception):
    pass


class Distance:

    def __init__(self, distance_func):
        self.distance_func = distance_func
       

    def unicode_normalization(self, text, form='NFKC'):
        return unicodedata.normalize(form, text)
    
    
    def scores(self, seq1, seq2):
        _get_scores = functools.partial(self.get_scores, seq2=seq2)
        for s1 in seq1:
            results = _get_scores(s1)
            yield results


    def get_scores(self, s1, seq2):
        scores = {s2: self.distance_func(s1, s2) for s2 in seq2}
        return {**dict(text=s1), **scores}
        # return scores


    def judge(self, dist1, dist2):
        """
        Override this method in subclasses
        to use candidate and multiprocess_candidate methods.
        """
        pass


    def candidate(self, seq1, seq2):
        _get_candidate = functools.partial(self.get_candidate, seq2=seq2)
        for s1 in seq1:
            result = _get_candidate(s1)
            yield result
            

    def get_candidate(self, s1, seq2):
        candidate = ''
        judged_dist = None
        for s2 in seq2:
            dist = self.distance_func(s1, s2)
            if not judged_dist or self.judge(dist, judged_dist):
                judged_dist = dist
                candidate = s2
        return dict(text=s1, candidate=candidate)


    def multiprocess_scores(self, seq1, seq2):
        _get_scores = functools.partial(self.get_scores, seq2=seq2)
        yield from self.handle_procecces(_get_scores, seq1, seq2)
        

    def multiprocess_candidate(self, seq1, seq2):
        _get_candidate = functools.partial(self.get_candidate, seq2=seq2)
        yield from self.handle_procecces(_get_candidate, seq1, seq2)
        

    def handle_procecces(self, func, seq1, seq2):
        jobs = multiprocessing.JoinableQueue()
        results = multiprocessing.Queue()
        self.create_processes(jobs, results, func)
        self.add_jobs(jobs, seq1)
        jobs.join()
        while not results.empty():
            result = results.get_nowait()
            yield result
        

    def create_processes(self, jobs, results, worker_func):
        for _ in range(multiprocessing.cpu_count()):
            process = multiprocessing.Process(
                target=self.work,
                args=(jobs, results, worker_func)
            )
            process.daemon = True
            process.start()


    def add_jobs(self, jobs, seq1):
        for s1 in seq1:
            jobs.put(s1)


    def work(self, jobs, results, worker_func):
        while True:
            try:
                s1 = jobs.get()
                result = worker_func(s1)
                results.put(result)
            finally:
                jobs.task_done()


    def scores_to_file(self, records, dir, file_type='xlsx'):
        self.output('scores', records, dir, file_type)


    def candidate_to_file(self, records, dir, file_type='xlsx'):
        self.output('candidate', records, dir, file_type)
          

    def output(self, data_type, records, dir, file_type):
        if file_type == 'xlsx':
            handler = ExcelHandler(dir, data_type)
        elif file_type == 'txt':
            handler = TextFileHandler(dir, data_type)
        elif file_type == 'csv':
            handler = CsvHandler(dir, data_type)
        else:
            raise FileTypeError(
                f'file_type must be xlsx or txt or csv: got {file_type}')
        handler.output(records)
        

def unicode_normalization_form(text):
    results = []
    forms = ['NFC', 'NFD', 'NFKC', 'NFKD']
    results.append(forms)
    results.append([unicodedata.normalize(form, text) for form in forms])
    results.append([str(unicodedata.normalize(form, text).encode('utf-8')) for form in forms])
    return results


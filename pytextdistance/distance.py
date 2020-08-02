import functools
import multiprocessing
import unicodedata


class Distance:

    def __init__(self, func):
        self.func = func

    
    def unicode_normalization(self, text, form='NFKC'):
        return unicodedata.normalize(form, text)
    
    
    def scores(self, seq1, seq2):
        get_scores = functools.partial(self._scores, seq2=seq2)
        for s1 in seq1:
            scores = get_scores(s1)
            yield s1, scores


    def _scores(self, s1, seq2):
        scores = {s2: self.func(s1, s2) for s2 in seq2}
        return scores


    def multiprocess_scores(self, seq1, seq2):
        get_scores = functools.partial(self._scores, seq2=seq2)
        jobs, results = self.create_queue()
        self.create_processes(jobs, results, get_scores)
        self.add_jobs(jobs, seq1)
        jobs.join()
        while not results.empty():
            result = results.get_nowait()
            s1, score = result
            yield s1, score
        

    def create_queue(self):
        jobs = multiprocessing.JoinableQueue()
        results = multiprocessing.Queue()
        return jobs, results


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
                distance = worker_func(s1)
                results.put((s1, distance))
            finally:
                jobs.task_done()


def unicode_normalization_form(text):
    results = []
    forms = ['NFC', 'NFD', 'NFKC', 'NFKD']
    results.append(forms)
    results.append([unicodedata.normalize(form, text) for form in forms])
    results.append([str(unicodedata.normalize(form, text).encode('utf-8')) for form in forms])
    return results



if __name__ == '__main__':
    from cyjarowinkler import jaro, jaro_winkler
    seq1 = ['James', 'Harold', 'Jaxon']
    seq2 = ['Carol', 'Jane', 'Joson', 'Jack', 'Harry']
    dist = Distance(jaro_winkler)
    for s1, scores in dist.multiprocess_scores(seq1, seq2):
        print(s1, scores)


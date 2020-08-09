import functools
import multiprocessing
import unicodedata


class Distance:

    def __init__(self, distance_func):
        self.distance_func = distance_func
       

    def unicode_normalization(self, text, form='NFKC'):
        return unicodedata.normalize(form, text)
    

    def scores(self, seq1, seq2):
        get_scores = functools.partial(self._scores, seq2=seq2)
        for s1 in seq1:
            scores = get_scores(s1)
            yield s1, scores


    def _scores(self, s1, seq2):
        scores = {s2: self.distance_func(s1, s2) for s2 in seq2}
        return scores


    def candidate(self, seq1, seq2):
        get_candidate = functools.partial(self._candidate, seq2=seq2)
        for s1 in seq1:
            candidate = get_candidate(s1)
            yield s1, candidate


    def _candidate(self, s1, seq2):
        candidate = ''
        judged_dist = None
        for s2 in seq2:
            dist = self.distance_func(s1, s2)
            if not judged_dist or self._judge(dist, judged_dist):
                judged_dist = dist
                candidate = s2
        return candidate


    def multiprocess_scores(self, seq1, seq2):
        get_scores = functools.partial(self._scores, seq2=seq2)
        for s1, score in self.handle_procecces(get_scores, seq1, seq2):
            yield s1, score


    def multiprocess_candidate(self, seq1, seq2):
        get_candidate = functools.partial(self._candidate, seq2=seq2)
        for s1, candidate in self.handle_procecces(get_candidate, seq1, seq2):
            yield s1, candidate


    def handle_procecces(self, func, seq1, seq2):
        jobs, results = self.create_queue()
        self.create_processes(jobs, results, func)
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


    def _judge(self, dist1, dist2):
        raise NotImplementedError()
        

def unicode_normalization_form(text):
    results = []
    forms = ['NFC', 'NFD', 'NFKC', 'NFKD']
    results.append(forms)
    results.append([unicodedata.normalize(form, text) for form in forms])
    results.append([str(unicodedata.normalize(form, text).encode('utf-8')) for form in forms])
    return results

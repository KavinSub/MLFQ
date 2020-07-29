from collections import defaultdict

from job import Job
from queue import Queue
from sequence import Sequence

PRIORITY_MAX = 5
PRIORITY_MIN = 0

# The amount of time a process is allotted in a queue at each priority level
# i.e. BUDGETS[i] for i in {0, 1, ..., 5} is how much time the process is allowed to
# spend in the queue of priority i before being demoted to a lower priority queue
BUDGETS = [float('inf'), 250, 200, 150, 100, 50]

# The size of a time slice for each queue
TIME_SLICES = [100, 50, 40, 30, 20, 10]

# How often the MLFQ should periodically boost processes to the topmost queue
# to avoid process starvation
BOOSTING_PERIOD = 1000

class MLFQ:
    def __init__(self, jobs: [Job]):
        self.queues = [Queue() for i in range(PRIORITY_MIN, PRIORITY_MAX + 1)]
        self.current_priority = PRIORITY_MAX

        self.accounting = defaultdict(lambda: BUDGETS.copy())
        self.active_jobs = len(jobs)

        self.job_ids = Sequence(1, lambda x: x + 1)

        for job in jobs:
            job_id = self.job_ids.gen()
            self.queues[self.current_priority].enqueue((job_id, job))

        self.events = []

        self.time_since_boost = 0

    def run(self):
        while self.active_jobs > 0:
            job_id, job = self.queues[self.current_priority].dequeue()

            time_slice = TIME_SLICES[self.current_priority]
            runtime = job.run(time_slice)

            self.accounting[job_id][self.current_priority] -= runtime
            self.time_since_boost += runtime
            
            self.events.append((job_id, 'run', runtime))

            # Handle job that just ran
            if job.done():
                self.active_jobs -= 1
            elif self.accounting[job_id][self.current_priority] <= 0:
                self.queues[self.current_priority - 1].enqueue((job_id, job))
            else:
                self.queues[self.current_priority].enqueue((job_id, job))

            # If we've exceeded the boost period, move all processes to the highest priority queue
            if self.time_since_boost > BOOSTING_PERIOD:
                for queue in self.queues[PRIORITY_MIN:PRIORITY_MAX]:
                    while len(queue) > 0:
                        self.queues[PRIORITY_MAX].enqueue(queue.dequeue())
                self.time_since_boost = 0
                    
            # Find the highest priority queue that is currently non-empty
            for i in range(PRIORITY_MIN, PRIORITY_MAX + 1)[::-1]:
                if len(self.queues[i]) > 0:
                    self.current_priority = i
                    break
        
        return self.events
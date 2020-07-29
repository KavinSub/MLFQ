import unittest

from distribution import Constant
from job import Job
from mlfq import MLFQ

class TestMLFQ(unittest.TestCase):
    def test_basic_functionality(self):
        job_1 = Job(50, Constant(5))
        job_2 = Job(100, Constant(10))

        mlfq = MLFQ([job_1, job_2])

        events = mlfq.run()

        self.assertEqual(events, [
            (1, 'run', 5),
            (2, 'run', 10),
            (1, 'run', 5),
            (2, 'run', 10),
            (1, 'run', 5),
            (2, 'run', 10),
            (1, 'run', 5),
            (2, 'run', 10),
            (1, 'run', 5),
            (2, 'run', 10),
            (1, 'run', 5),
            (1, 'run', 5),
            (1, 'run', 5),
            (1, 'run', 5),
            (1, 'run', 5),
            (2, 'run', 10),
            (2, 'run', 10),
            (2, 'run', 10),
            (2, 'run', 10),
            (2, 'run', 10)
        ])

if __name__ == '__main__':
    unittest.main()
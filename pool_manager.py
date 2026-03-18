from multiprocessing import Pool
from worker import Worker
import logging

logger = logging.getLogger(__name__)

def running_worker(job):
    worker = Worker(job)
    return worker.pipeline_execution()

class PoolManager:

    def __init__(self, job_description):
        self._job_description = job_description
        
    

    def pool_operations(self):
        try:
            with Pool() as pool:
                result = pool.map(running_worker, self._job_description)
                return result
        except Exception as e:
            msg = f"Pool operation failed: {str(e)}"
            logger.error(msg)
            return []
        
from multiprocessing import Pool
from worker import Worker
import logging
from typing import List, Dict, Any

logger = logging.getLogger(__name__)

def running_worker(job: Any) ->Dict[str, Any]:
    """
    A seperated function from the class thats needed for multiprocessing
    to pick up and carryout the worker pipeline in its own seperate process.
    """
    worker = Worker(job)
    return worker.pipeline_execution()

class PoolManager:
    """
    Coordination of the distribution process for ticker jobs to the multiprocessing Pool
    """

    def __init__(self, job_description: List[Any]):
        self._job_description = job_description
        
    

    def pool_operations(self) -> List[Dict[str, Any]]:
        try:
            #using a context manager for the pool to make sure thart all processes are cleaned after jobs end
            with Pool() as pool:
                #distribution of the jobs across the available cpu cores
                result = pool.map(running_worker, self._job_description)
                return result
        except Exception as e:
            msg = f"Pool operation failed: {str(e)}"
            logger.error(msg)
            return []
        
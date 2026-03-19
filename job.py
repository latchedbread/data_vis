

class Job:
    """
    a container that will hold the parameters for a singular stock processing task.
    """
    def __init__(self, ticker_symbol: str, start_date: str, end_date: str, db_path: str):
        self._ticker_symbol = ticker_symbol
        self._start_date = start_date
        self._end_date = end_date
        self._db_path = db_path
    
    #getters for private attributes
    #getters for stronger robustness
    @property
    def ticker(self) -> str:
        return self._ticker_symbol
    
    @property
    def start_date(self) -> str:
        return self._start_date
    
    @property
    def end_date(self) -> str:
        return self._end_date
    
    @property
    def db_path(self) -> str:
        return self._db_path



class Job:
    def __init__(self, ticker_symbol, start_date, end_date, db_path):
        self._ticker_symbol = ticker_symbol
        self._start_date = start_date
        self._end_date = end_date
        self._db_path = db_path
    
    #getters for private attributes
    #getters for stronger robustness
    @property
    def ticker(self):
        return self._ticker_symbol
    
    @property
    def start_date(self):
        return self._start_date
    
    @property
    def end_date(self):
        return self._end_date
    
    @property
    def db_path(self):
        return self._db_path

import sqlite3
import pandas as pd
import logging

logger = logging.getLogger(__name__)

class DataBaseClient:
    
    def __init__(self, ticker, db_name):
        self._ticker = ticker
        self._db_name = db_name
        self._pricelist = []
    

    def price_querying(self):
        try:
            with sqlite3.connect(self._db_name) as conn:
                sql_query = f"SELECT Close FROM {self._ticker}"
                df = pd.read_sql_query(sql_query, conn)
                if df.empty:
                    msg = f"No data was found in the table {self._ticker}"
                    logger.warning(msg)
                    return self._pricelist, msg
                else:
                    self._pricelist = df['Close'].tolist()
                    return self._pricelist, None  
        except Exception as e:
            msg = f"The following error has occurred: {e} please try again."
            logger.error(msg)
            return [], msg
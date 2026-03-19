import sqlite3
import pandas as pd
import logging
from typing import List, Tuple

logger = logging.getLogger(__name__)

class DataBaseClient:
    """
    This will handle the querying of the SQLite db to get specefic price series.
    """
    
    def __init__(self, ticker: str, db_name: str):
        self._ticker = ticker
        self._db_name = db_name
       
    

    def price_querying(self) -> Tuple[List[float], str | None]:
        try:
            with sqlite3.connect(self._db_name) as conn:
                #this only queries the Close column thats needed for trend anaylsis
                sql_query = f"SELECT Close FROM {self._ticker}"
                df = pd.read_sql_query(sql_query, conn)
                if df.empty:
                    msg = f"No data was found in the table {self._ticker}"
                    logger.warning(msg)
                    return [], msg
                else:
                    #conversion series to a list in order to keep the analyzer seperated from pandas.
                    pricelist = df['Close'].tolist()
                    return pricelist, None  
        except Exception as e:
            msg = f"The following error has occurred: {e} please try again."
            logger.error(msg)
            return [], msg
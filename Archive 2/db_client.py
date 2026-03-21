import sqlite3
import pandas as pd
import logging
import re
from typing import List, Tuple

logger = logging.getLogger(__name__)

class DataBaseClient:
    """
    This will handle the querying of the SQLite db to get specific price series.
    """
    
    def __init__(self, ticker: str, db_name: str):
        self._ticker = ticker
        self._db_name = db_name
       
    

    def query_prices(self) -> Tuple[List[float], str | None]:
        try:
            #cleaning of the ticker and added a timeout for concurrent  safety
            safe_name = re.sub(r'[^a-zA-Z0-9_]', '', self._ticker)
            
            with sqlite3.connect(self._db_name) as conn:
                #this only queries the Close column thats needed for trend anaylsis
                sql_query = f"SELECT Close FROM {safe_name}"
                df = pd.read_sql_query(sql_query, conn)
                if df.empty:
                    msg = f"No data was found in the table {safe_name}"
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
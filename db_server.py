
import sqlite3
import logging

logger = logging.getLogger(__name__)

class DataBaseServer:

    def __init__(self,dataframe, ticker, db_name):
        self._dataframe = dataframe
        self._ticker = ticker
        self._db_name = db_name
    

    def table_create_store(self):
        try:
        
            with sqlite3.connect(self._db_name) as conn:
                table_name = self._ticker
                self._dataframe.to_sql(table_name, conn, if_exists="replace", index=False )
            return None
        except Exception as e:
            msg = f"The following error has occurred: {e} please try again."
            logger.error(msg)
            return msg
            
            

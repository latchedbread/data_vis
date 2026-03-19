
import sqlite3
import logging

logger = logging.getLogger(__name__)

class DataBaseServer:
    """
    handling of "Store" phase of this pipeline by  moving dfs into SQLite
    """

    def __init__(self, ticker, db_name):
        #only storing config, nit actual date to ensure the classes modularity
        self._ticker = ticker
        self._db_name = db_name
    

    def table_create_store(self, data_frame) -> str | None:
        try:
            #context manager to ensure proper connection closure
            with sqlite3.connect(self._db_name) as conn:
                table_name = self._ticker
                #the use of replace makes sure that fresh scrapes will replace any bad/stale data in the db
                data_frame.to_sql(table_name, conn, if_exists="replace", index=False )
            return None
        except Exception as e:
            msg = f"The following error has occurred: {e} please try again."
            logger.error(msg)
            return msg
            
            

import pandas as pd
import yfinance as yf
import logging

logger = logging.getLogger(__name__)

class WebScraper:

    def __init__(self, ticker):
        self._ticker = ticker
    

    def data_fetcher(self, start_date, end_date):
        #calling the helper method
        #making sure the dates are good
        warning = self._date_validation(start_date, end_date)
        if warning != None:
            logger.warning(warning)
            return pd.DataFrame(), warning
        else:
            df = yf.download(self._ticker, start=start_date, end=end_date)
            
            if df.empty:
                msg = f"No data found for ticker {self._ticker}"
                logger.warning(msg)
                return pd.DataFrame(), msg
            else:
                df.columns = df.columns.get_level_values(0)
                return df, None
                
    
    def _date_validation(self, start_date, end_date):
        if start_date <= end_date:
            return None
        else:
            return f"Warning!! The start date {start_date} is after the end date:{end_date} make sure the dates are correct."



        
        
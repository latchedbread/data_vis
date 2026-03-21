import pandas as pd
import yfinance as yf
import logging
from typing import Tuple

logger = logging.getLogger(__name__)

class WebScraper:
    """
    Handling of the scrape phase by getting the data from Yf
    """

    def __init__(self, ticker: str):
        self._ticker = ticker
    

    def scrape(self, start_date: str, end_date: str) -> Tuple[pd.DataFrame, str | None]:
            
            #trusting the dates since the gui has already validated them
            df = yf.download(self._ticker, start=start_date, end=end_date)
            
            if df.empty:
                msg = f"No data found for ticker {self._ticker}"
                logger.warning(msg)
                return pd.DataFrame(), msg
            else:
                #cleaning of the colun levels ensuring the df's are easier for the analyzer to read.
                df.columns = df.columns.get_level_values(0)
                return df, None
                
    
    


        
        
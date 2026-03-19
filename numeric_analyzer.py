import pandas as pd
import numpy as np
import logging
from typing import List, Tuple

logger = logging.getLogger(__name__)

class NumericAnalyzer:
    """
    We can handle the analysis phase by calculating the linear trend for the price series!
    """

    #init was not needed, since this class doesn't hold any state.

    
    def compute_numeric_trend(self, price_list: List[float]) -> Tuple[pd.DataFrame, str | None]:
        prices = np.array(price_list)
        
        #atleast 2 days of data r needed to define the trend line
        if len(price_list) < 2:
            msg = "Not enough data to compute a trend line."
            logger.warning(msg)
            #fallback is just a trendline that mirrors the actual price
            df = pd.DataFrame({"index": np.arange(len(prices)), 
                "actual": price_list, "trend": prices})
            return df, msg

        #index for x-axis
        indx = np.arange(len(prices))


        m, b = np.polyfit(indx, prices, 1)
        trend = m * indx + b
        #computation of optional metrics
        mse = float(np.mean((prices - trend) **2))
        r2 = float(
            1 - np.sum((prices - trend)**2)/
            np.sum((prices - np.mean(prices))**2)
        )

        #assemble plot ready df

        df = pd.DataFrame({
            "index": indx,
            "actual": prices,
            "trend": trend
        })
        #return the values
        return df, None
        

    


import pandas as pd
import numpy as np
import logging

logger = logging.getLogger(__name__)

class NumericAnalyzer:

    def __init__(self, price_list):
        self._price_list = price_list

    
    def compute_numeric_trend(self):
        prices = np.array(self._price_list)
        #numeric index creation
        if len(self._price_list) < 2:
            msg = "Not enough data to compute a trend line."
            logger.warning(msg)
            df = pd.DataFrame({"index": np.arange(len(prices)), 
                "actual": self._price_list, "trend": prices})
            return df, msg

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
        

    


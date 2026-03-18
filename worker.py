from webscraper import WebScraper
from db_server import DataBaseServer
from db_client import DataBaseClient
from numeric_analyzer import NumericAnalyzer
import pandas as pd
import logging

logger = logging.getLogger(__name__)

class Worker:

    def __init__(self, job):
        self._job = job

    def pipeline_execution(self):

        try:
            #scrape the data
            scraper = WebScraper(self._job.ticker)
            scraped_df, scraping_warning = scraper.data_fetcher(self._job.start_date, self._job.end_date)

            #storing the data
            store_warning = DataBaseServer(scraped_df, self._job.ticker, self._job.db_path)
            store_warning = store_warning.table_create_store()

            #executing the query
            client = DataBaseClient(self._job.ticker, self._job.db_path)
            prices, query_warning = client.price_querying()

            #Analysis
            analyzer = NumericAnalyzer(prices)
            plot_df, analysis_warning = analyzer.compute_numeric_trend()

            #Package the result
            warning_list = [scraping_warning, store_warning, query_warning, analysis_warning]
            warning_list = [w for w in warning_list if w]

            return {
                "ticker": self._job.ticker,
                "plot_df": plot_df,
                "warnings": warning_list
            }
        except Exception as e:
            msg = f"Worker failed for ticker {self._job.ticker}: {str(e)}"
            logger.error(msg)
            return {
                "ticker": self._job.ticker,
                "plot_df": pd.DataFrame(),
                "warnings": [msg]
            }





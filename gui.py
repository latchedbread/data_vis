import tkinter as tk
from tkinter import messagebox
import logging
import matplotlib.pyplot as plt
from datetime import datetime
from typing import List

# Internal module imports
from pool_manager import PoolManager
from graph_plotter import GraphPlotter
from job import Job


logger = logging.getLogger(__name__)

class Gui:
    """
    This is the main interface that the user uses.
    It will handle: input collection, validation, and the triggering of the backend pipeline.
    """
    def __init__(self, window:tk.Tk, db_path: str="stocks.db"):
        #boilerplate code implemented with ai assistance(as allowed in instructions)
        self._db_path = db_path
        self._window = window

        self._window.title("Stock Data Visualizer")

        # Start date
        tk.Label(window, text="Start Date (YYYY-MM-DD):").pack()
        self._start_date_entry = tk.Entry(window)
        self._start_date_entry.pack()

        # End date
        tk.Label(window, text="End Date (YYYY-MM-DD):").pack()
        self._end_date_entry = tk.Entry(window)
        self._end_date_entry.pack()

        # Ticker listbox
        tk.Label(window, text="Select Tickers:").pack()
        self._ticker_listbox = tk.Listbox(window, selectmode=tk.MULTIPLE)
        self._ticker_listbox.pack()

        # Populate tickers
        for ticker in self._dow_jones_tickers():
            self._ticker_listbox.insert(tk.END, ticker)

        # Submit button
        tk.Button(window, text="Submit", command=self._on_submit).pack()
    
    def _dow_jones_tickers(self) -> List[str]:
        #the list of tickers for this assingment
        return [
            "AAPL", "AMGN", "AXP", "BA", "CAT",
            "CRM", "CSCO", "CVX", "DIS", "DOW",
            "GS", "HD", "HON", "IBM", "INTC",
            "JNJ", "JPM", "KO", "MCD", "MMM",
            "MRK", "MSFT", "NKE", "PG", "TRV",
            "UNH", "V", "VZ", "WBA", "WMT"
        ]
    
    def _on_submit(self) -> None:

        start_date = self._start_date_entry.get()
        end_date = self._end_date_entry.get()

        #validation for dates before any work happens to save resources
        if not self._validate_dates(start_date, end_date):
            messagebox.showerror("Error", "Invalid date format! Please use YYYY-MM-DD")
            return

        selected_tickers = [self._ticker_listbox.get(i) for i in self._ticker_listbox.curselection()]

        if not selected_tickers:
            messagebox.showwarning("Warning", "Please select at least one ticker!")
            return
        
        #creation of job objects that will get passed into the pool
        job_obj_list = [] 
        for ticker in selected_tickers:
            job_obj = Job(ticker,start_date, end_date, self._db_path)
            job_obj_list.append(job_obj)
        
        try:
            pool = PoolManager(job_obj_list)
            results = pool.pool_operations()

            has_plots = False #making sure if we actually generated any graphs

            for result in results:
                #only plot if the worker actually returns data
                if not result["plot_df"].empty:
                    graph = GraphPlotter(result["ticker"], result["plot_df"])
                    graph.graph_displayment()
                    has_plots = True
                if result["warnings"]:
                    messagebox.showwarning("Warning", "\n".join(result["warnings"]))
            #allows background graphs to pop up all at the same time if the user desires.
            if has_plots:
                plt.show()
        except Exception as e:
            msg = f"An error occurred while processing: {str(e)}"
            logger.error(msg)
            messagebox.showerror("Error", msg)


    def _validate_dates(self, start_date: str, end_date: str) -> bool:
        try:
            start = datetime.strptime(start_date, "%Y-%m-%d")
            end = datetime.strptime(end_date, "%Y-%m-%d")
            #additional safety check
            if start > end:
                return False
            
            return True
        except ValueError:
            return False

        



        

Stock Data Visualization - Aidan McCullough


Project Design:

-Statelessness(a previously made error on past assignments):
    -to make sure for having thread-safety for mulitprocessing,
        all worker classes(DataBaseServer, NumericAnalyzer, etc) are stateless.
    -All of the data gets passed directly into methods instead of being stored inside the constructors


-Input Validation:
    -The GUI has strict date validation to catch possible errors by the user before spawning workers.


-Pipeline archeticture:
    -Implemented a "short-circuit" in the worker class to start running right away if the WebScraper doesn't find any data
    -this ensures no unnessary database operations get carried out


-Non-Blocking UI:
    -the graph plotter prepares the figures in the background and calls plt.show() only after the entire job pool
    -this prefents the Tkinter interface from freezing

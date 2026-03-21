Stock Data Visualization - Aidan McCullough


Project Overview:

This is a high-preforming multi-threaded stock anaylsis tool that fetches historical data,
and then stores it inside of a sanitzed SQLite db.

Architectural Design:
-Non-Blocking Mulithreaded GUI:
    implementation of the threading module. THe worker thread manages the multiprocessing pool,
    which keeps the interface responsive and stocks possible errors like Application Not Responding" during heavy data fetching.

-Configuration File:
    moved all of the hardcoded constants(the tickers) into one seperate file to improve the scalability of this project.

-Sanitation on Database Operations:
    Added the use of regex based ticker sanitization. This was to protect against any possible SQL injections.I also added a 10 second connection timeout
    to make sure thread safe concurrent writes to the SQL database.

-Stateless Worker Pipeline:
    To confirm thread safety for multiprocessing, all of the processing classes are stateless(a mistake made on previous exercises). Data gets passed straight into the methods
    instead of being stored in instance attributes.
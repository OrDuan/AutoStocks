AutoStocks
====================

AutoStocks Project has 3 steps of developing for stage 1:

Downloader:
==========
The downloader is a class that will download stocks information 
with multi-threading, all of the information is stored on a DB for future steps.

Stargerties:
==========
The strategy class is made for iterate the DB information, each strategy will have a different code which will be guided by different algorithms to buy and sell stocks. We will use a inner-app money to check the best results between the stargerties.

LIVE:
==========
After finding the bests stargerties we will take them forward. We will change the downloader and stargerties classes to work asynchrony on live stocks.


Future Developing - Stage 2: 
==========
These 3 steps should give us reports and predictions so we can calculate the incomes with inner-app money. Now we will re-code the app so we will use an API to buy and sell REAL stocks.

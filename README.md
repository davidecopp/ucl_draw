# ucl_draw

Since I always wanted to predict Champions League Round of 16, here the need to share this repo.
This repo can be used for every draw of the knock-out stage of every tournament, e.g. Champions League or Europa League.
The algorithm is based on the Monte Carlo method and the frequentist theory of probability: a set number of valid draws are done, and after that the occurences of each drawn match are counted. 
Dividing the number of occurences for the wanted number of valid draws, we obtain the "probability" of a given match.
Higher the set number of draws, closer to the real probabilities the frequence-based probabilities are.
I applied the algorithm to the teams of the Champions League 2018-19 Round of 16.

The files inside the repo are:

* ucl_draw_functions.py
* main.py
* teams.csv
* out:
  * draws.txt
  * ucl_results_table.csv
  * ucl_results.txt 

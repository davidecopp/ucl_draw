import pandas as pd
import ucl_functions as ucl

# Reading input csv
data = pd.read_csv("teams.csv", index_col="TEAM")
teams_1 = list(data[data["FASCIA"]==1].index)
teams_2 = list(data[data["FASCIA"]==2].index)
nations = data.to_dict(orient='dict')['NATION']
groups = data.to_dict(orient='dict')['GROUP']

# Set the number of valid draws wanted
n_valid_draws_target = 100000

# Perform the draws
n_valid_draws = 0
file = open("out/draws.txt", "w")
while n_valid_draws < n_valid_draws_target:
    matchups, valid_draw_flag = ucl.perform_draw(teams_1[:], teams_2[:], groups, nations)
    n_valid_draws += valid_draw_flag
    with open('out/draws.txt', 'a') as file:
        ucl.write_draws(file, matchups, valid_draw_flag)
ucl.write_results(n_valid_draws_target)

# Write draws probability table
df = pd.read_csv("out/ucl_results.txt", sep="\t", names=["HomeTeam", "AwayTeam", "Number"])
df = df.pivot(index="HomeTeam", columns="AwayTeam", values="Number")
df.to_csv("out/ucl_results_table.csv")

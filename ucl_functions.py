import random 

def is_valid_matchup(team_1, team_2, groups, nations):
    is_valid_flg = groups[team_1] != groups[team_2] and nations[team_1] != nations[team_2] 
    return is_valid_flg

def perform_draw(teams_1, teams_2, groups, nations, max_attempts=10000):
    matchups = []
    attempts = 0
    while len(teams_1) > 0 and attempts <= max_attempts:
        team_1 = random.choice(teams_1)
        team_2 = random.choice(teams_2)
        if is_valid_matchup(team_1, team_2, groups, nations):
            matchups.append([team_1, team_2])
            teams_1.remove(team_1)
            teams_2.remove(team_2)
        else:
            attempts += 1
    valid_draw_flag = attempts <= max_attempts
    return(matchups, valid_draw_flag)

def write_draws(file, matchups, valid_draw_flag):
    if valid_draw_flag:
        for match in matchups:
            file.write(f'{match[0]}\t{match[1]}\n')    
    else: 
        file.write('NOT VALID \n')
    return 0

def write_results(n_valid_draws_target):
    combinations_count = {}
    with open('out/draws.txt', 'r') as file:
        matches = file.read().splitlines()
    for match in matches:
        if "NOT VALID" not in match:
            combinations_count[match] = combinations_count.get(match, 0) + 1
    file = open("out/ucl_results.txt", "w")
    combinations_count = dict(sorted(combinations_count.items(), key=lambda item: item[1], reverse=True))
    for match in combinations_count:
        file.write(f'{match}\t{combinations_count[match]/n_valid_draws_target} \n')
    return combinations_count

# What the problem is teaching:

# Using a dict as a scoreboard (frequency/accumulation pattern)
# Syncing two arrays by index with enumerate
# Keeping a running "current best" so you don't need a second pass to find the max




# competition = [
#     ["HTML","C#"],
#     ["C#","PYTHON"],
#     ["PYTHON","HTML"]

# ]
# results = []
# for match in competition:
#     home, away = match
#     print(home,away)
#     if len(home) > len(away):
#         results.append(home)
#     elif len(away) > len(home):
#         results.append(away)
#     else: 
#         results.append("Tie")

# print(results)

    # for teams in match:





# for matches in competition:
#     for k, len(k)  in matches.items():
#         print(k,len(k))



        # winner = max(team_len)
        # print(winner)
        # max

# dict = {
# "jude": "mnoma"
# }
# print(dict)
# dict.update({"meow": 5})

# print(dict)

# competition = [
#     ["HTML","C#"],
#     ["C#","PYTHON"],
#     ["PYTHON","HTML"]

# ]
# results = [0,0,1]
# # best_team = #'highest score at the time' 
# scores = {" ": 0, }

# print(home, away


# tournament winner

# competition[in a 1 layer deep array], the results of the competition in an array
# I want to see which team got the most points. The best winner.
# 
competitions = [
    ["HTML","C#"], 
    ["C#","PYTHON"],
    ["PYTHON","HTML"]
#      HOME     AWAY
]

HOME_TEAM_WON = 1
results = [0,1,1]
# winning team and current best team are different
def tournamentwinner(competitions,results):
    currentBestTeam= ""
    scores = {currentBestTeam: 0}

    for idx, competition in enumerate(competitions):
     result = results[idx]
     home, away = competition 
     winningTeam = home if result == HOME_TEAM_WON else away
       
    #  if result == HOME_TEAM_WON:
    #     print(f"Home won {home}")
    #     winningTeam = home
    #  else:
    #     print (f"Away team won {away}")
    #     winningTeam = away

    updatescores(winningTeam, 3,scores)
    if scores[winningTeam] > scores[currentBestTeam]:
        currentBestTeam = winningTeam

    return currentBestTeam
  
def updatescores(team, points,scores):
   if team is not scores:
    scores[team] = scores.get(team, 0) + points
  
tournamentwinner(competitions,results)
       

#using a dictionary as a scoreboard
# if it's python the value ndio inachange

# scores = {}
# scores[team] = scores.get(team, 0) + points
# What it is: Using a dict to count or accumulate values keyed by some identifier.

# The mental trigger: Anytime a problem says "track score / count / frequency per item" → reach for this immediately.4. Safe Dict Initialization
# 4. Safe Dict Initialization
# python
# if team not in scores:
#     scores[team] = 0
# scores[team] += points

# # Or the Pythonic shorthand:
# scores[team] = scores.get(team, 0) + points
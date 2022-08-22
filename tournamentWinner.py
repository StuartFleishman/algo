HOME_TEAM_WINNING = 1
#O(n) time 
#O(k) space 
def tournamentWinner(competitions, results):
    currentBestTeam = ""
    scores = {currentBestTeam: 0}

    for idx, competition in enumerate(competitions):
        result = results[idx]
        homeTeam, awayTeam = competition

        winningTeam = homeTeam if result == HOME_TEAM_WINNING else awayTeam

        updateScores(winningTeam, 3, scores)

        if scores[winningTeam] > scores[currentBestTeam]:
            currentBestTeam = winningTeam
    return currentBestTeam


def updateScores(team, points, scores):
    if team not in scores:
        scores[team] = 0

    scores[team] += points

#competitions [homeTeam, awayTeam]
competitions = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]

# 0 means awayTeam won, 1 means homeTeam won
#win = 3 points
results = [0, 0, 1]

print(tournamentWinner(competitions, results))

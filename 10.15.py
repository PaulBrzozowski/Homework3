#UHID 2037080
#Paul Brzozowski
#CIS 2348
#FALL 2022
class Team:
    def __init__(self):
        self.teamN = 'None'
        self.team_wins = 0.0
        self.team_loses = 0.0

    def get_win_percentage(self):
        try:
            x = self.team_wins / (self.team_wins + self.team_loses)
            return x
        except ZeroDivisionError:
            x = 0.0
            return x


if __name__ == '__main__':
    team = Team()
    teamN = input()
    teamWs = float(input())
    teamLs = float(input())
    team.teamN = teamN
    team.team_wins = teamWs
    team.team_loses = teamLs

    if team.get_win_percentage() >= 0.5:
        print('Congratulations, Team', team.teamN, 'has a winning average!')
    else:
        print('Team', team.teamN, 'has a losing average.')
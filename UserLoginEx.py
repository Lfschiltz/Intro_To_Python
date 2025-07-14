import datetime


class User:
    def __init__(self, uname, pword):
        self.username = uname
        self.password = pword

        self.activeUser = True
        self.numOfLogins = 0
        self.dateJoined = datetime.date.today()

    # display number of logins
    def show_num_logins(self):
        return self.username + " logged in " + str(self.numOfLogins) + " times."
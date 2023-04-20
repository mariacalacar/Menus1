from Student import Student

class Grade(Student):
    def __init__(self, History, Architecture, Netcom, Purcom) -> None:
        self.History = History
        self.Architecture = Architecture
        self.Netcom = Netcom
        self.Purcom = Purcom

    def getAverage(self):
        return (int(self.History) + int(self.Architecture) + int(self.Netcom) + int(self.Purcom))/4
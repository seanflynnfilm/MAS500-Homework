class ElectionResults:
  
    def __init__(self, filename):
        self.filename = filename

    def load(self):
        self.file = open(self.filename, 'r')
        self.all_lines = self.file.readlines()
        self.data = []
        for line in self.all_lines:
            columns = line.split(',')
            self.data.append(columns)

    def states(self):
        all_names = []
        for line in self.all_lines:
            columns = line.split(',')
            all_names.append(columns[1])
        return all_names[1:]

    def state_count(self):
        return len(self.states())

    def vote_count(self):
        obamaVote = 0
        romneyVote = 0

        for i in range(1, len(self.all_lines)):
            obamaVote += int(self.data[i][3])
            romneyVote += int(self.data[i][5])

        vote_totals = {}
        vote_totals['Obama'] = obamaVote
        vote_totals['Romney'] = romneyVote

        return vote_totals

class Project:
    def __init__(self, project_name):
        self.name = project_name
        self.users = []
        self.entries = []

    def add_entry(self, username, start, stop, comment):
        if username not in self.users:
            self.users.append(username)

        self.entries.append(Entry(username, start, stop, comment))

    def get_report(self):
        return


class Entry:
    # TODO: Make me
    pass

if __name__ == '__main__':
    # TODO: Put the meat of the program here

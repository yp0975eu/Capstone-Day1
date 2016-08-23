from datetime import datetime

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
    #TODO: add start and stop time
    def __init__(self, name, time, comment):
        #self.start_time = start_time
        #self.end_time = end_time
        self.time = time
        self.comment = comment

    # TODO:
    # Store as a timestamp for starting and stopping
    # tell the difference between two timestamps

    @staticmethod
    def is_valid_time(hours):
        try:
            float(hours)
        except ValueError:
            print "Whoops, you need to enter an integer or float"
            return False

        return True


if __name__ == '__main__':
    #   TODO: Put the meat of the program here
    # Try to find a file
    # if there is no file, get project name and start a new file

    project_name = input("What is the project name?")
    # Overwrite for prototype
    project_name = "project"

    if Project.project_exists(project_name):
        project = ProjectDatabase.get_project(project_name)
    else:
        project = Project(project_name)

    # TODO
    #menu loop
    #process menu selection
    #if 1 add entry
    #if 2 show_report
    #if 3 quit

    pass


from datetime import datetime


class ProjectDatabase:
    @staticmethod
    def get_project(name):
        with open('{}.txt'.format(name), 'r') as f:
            project_name = f.readline()
            project = Project(project_name)
            for line in f:
                line_parts = line.split(';')
                username = line_parts[0]
                hours = line_parts[1]
                comment = line_parts[2]
                project.add_entry(username, hours, comment)


    @staticmethod
    def save_project(project):
        with open('{}.txt'.format(project.name), 'w') as f:
            f.write(project.name)
            for entry in project.entries:
                f.write('{};{};{}'.format(entry.name, entry.time, entry.comment))


    @staticmethod
    def project_exists(name):
        try:
            open('{}'.format(name))
        except IOError:
            return False

        return True


class Project:
    def __init__(self, project_name):
        self.name = project_name
        self.users = []
        self.entries = []

    def add_entry(self, username, time, comment):
        if username not in self.users:
            self.users.append(username)

        self.entries.append(Entry(username, time, comment))

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
        project = ProjectDatabase.create_new_project(project_name)

    pass

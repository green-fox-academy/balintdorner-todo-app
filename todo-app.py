import sys

class Control():

    def arg_reader(self):
        self.list_argv = []
        if len(sys.argv) <= 1:
            self.list_argv = []
        else:
            self.list_argv = sys.argv[1:]

        if len(self.list_argv) == 0:
            display.print_help()
        else:
            pass

class Model():
    pass



class Display():

    def print_help(self):
        print("Python Todo application \n ======================= \n \n Command line arguments: \n -l   Lists all the tasks \n -a   Adds a new task \n -r   Removes an task \n -c   Completes an task")

control = Control()
display = Display()

control.arg_reader()

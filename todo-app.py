import sys

class Control():

    def __init__(self):
        self.list_argv = []
        self.arg_reader()
        self.controller()


    def arg_reader(self):
        if len(sys.argv) <= 1:
            self.list_argv = []
        else:
            self.list_argv = sys.argv[1:]

    def controller(self):
        if len(self.list_argv) == 0:
            display.print_help()
        elif self.list_argv[0] == '-l':
            display.print_file()

class Model():

    def __init__(self):
        self.txt = ""
        self.adder()
#        self.txt_dict =

    def adder(self):
        my_file = open('database.txt', 'r')
        self.txt = my_file.readlines()
        my_file.close()

class Display():

    def print_help(self):
        print("Python Todo application \n ======================= \n \n Command line arguments: \n -l   Lists all the tasks \n -a   Adds a new task \n -r   Removes an task \n -c   Completes an task")

    def print_file(self):
        if len(model.txt) == 0:
            print("No todos for today! :)")
        else:
            for i in range(len(model.txt)):
                print(i+1, model.txt[i][:-1])



model = Model()
display = Display()
control = Control()

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
            elif self.list_argv[0] == '-c':
                try:
                    if len(self.list_argv) <= 1:
                        display.print_unable_to_check()
                    elif int(self.list_argv[1]) > len(model.txt):
                        display.print_unable_to_check()
                    else:
                        model.checker(int(self.list_argv[1]))
                        display.print_file()
                except:
                    display.print_unable_to_check()
            elif self.list_argv[0] == '-a':
                if len(self.list_argv) <= 1:
                    print('Unable to add: no task provided')
                else:
                    model.appender(self.list_argv[1])
                    display.print_file()
            elif self.list_argv[0] == '-r':
                try:
                    if len(self.list_argv) <= 1:
                        display.print_remove_error()
                    elif int(self.list_argv[1]) > len(model.txt):
                        display.print_remove_error()
                    else:
                        model.remover(int(self.list_argv[1]))
                except:
                    display.print_remove_error()
            else:
                print(" \n Unsupported argument \n")
                display.print_help()

class Model():

    def __init__(self):
        self.txt = ""
        self.opener()

    def opener(self):
        my_file = open('database.txt', 'r')
        self.txt = my_file.readlines()
        my_file.close()

    def open_write(self):
        my_file = open('database.txt', 'w')
        my_file.writelines(self.txt)
        my_file.close()

    def appender(self, thing):
        self.txt.append('[ ] ' + '||| ' + thing + '\n')
        self.open_write()

    def remover(self, element):
        del self.txt[element]
        self.open_write()

    def checker(self, element):
        self.txt[element] = '[x]' + self.txt[element][3:-1] + '\n'
        self.open_write()

class Display():

    def print_help(self):
        print("Python Todo application \n ======================= \n \n Command line arguments: \n -l   Lists all the tasks \n -a   Adds a new task \n -r   Removes an task \n -c   Completes an task")

    def print_file(self):
        if len(model.txt) == 0:
            print("No todos for today! :)")
        else:
            for i in range(len(model.txt)):
                print(i+1, model.txt[i][:-1])

    def print_remove_error(self):
        print("Unable to remove")

    def print_unable_to_check(self):
        print("Unable to check")

model = Model()
display = Display()
control = Control()

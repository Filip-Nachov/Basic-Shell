'''
MIT License

Copyright (c) 2024 Filip Nachov

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.'''

import os
import subprocess

# all shell commands
class Shell_commands:
    def exit_cmd(self):
        print("Ending shell session")
        exit(0)

    def echo_cmd(self, args):
        print(" ".join(args))

    def print_cmd(self, args):
        print(" ".join(args))

    def mkdir_cmd(self, name):
        os.makedirs(name)


    def ls_cmd(self, directory):
        files = os.listdir(directory)
        num = 0
        for i in files:
            num += 1
            print(f"file {num}: {i}")

    def pwd_cmd(self):
        path = os.getcwd()
        print(path)

    def cd_cmd(self, path):
        os.chdir(path)

    def rmdir_cmd(self, name):
        os.rmdir(name)

    def touch_cmd(self, name):
        open(name, "w")

    def rm_cmd(self, name):
        try:
            os.remove(name)
            print(f"File '{name}' deleted successfully.")
        except OSError as e:
            print(f"Error: {e}")

    def help_cmd(self):
        print("exit: exits the shell")
        print("pwd: shows your current path")
        print("cd: changes the current directory")
        print("ls: shows all the items in the current directory")
        print("echo or print <word/sentence>: prints out the word or sentences said")
        print("mkdir <name>: creates a directory with that name")
        print("rmdir <name>: deletes the directory registered under that name")
        print("touch <name>: make a file with that name") 
        print("rm <name>: delets the file under that name")

# the shell  working system
class Shell:
    def __init__(self):
        # defining all the commands from the Shell_commands class
        self.commands = {} # making a hashmap
        shell_commands = Shell_commands # connecting the class into a variable
        self.commands["exit"] = shell_commands.exit_cmd # exit command
        self.commands["echo"] = shell_commands.echo_cmd # echo command
        self.commands["print"] = shell_commands.print_cmd # print command
        self.commands["ls"] = shell_commands.ls_cmd # ls command
        self.commands["pwd"] = shell_commands.pwd_cmd # pwd commnad
        self.commands["cd"] = shell_commands.cd_cmd # cd command
        self.commands["help"] = shell_commands.help_cmd # help command
        self.commands["mkdir"] = shell_commands.mkdir_cmd # mkdir command
        self.commands["rmdir"] = shell_commands.rmdir_cmd # rmdir command
        self.commands["touch"] = shell_commands.touch_cmd # touch command
        self.commands["rm"] = shell_commands.rm_cmd # rm command
    def run(self):
        print('For all available commands type "help"')
        while True: # making a while loop for the input
            path = os.getcwd() # taking path
            inputing = input(f"$ {path}: ") # taking input
            if inputing == "exit": # the if system to run the wanted command
                self.commands["exit"](self) 
            elif inputing.startswith("echo"):
                args = inputing.split()[1:]
                self.commands["echo"](self, args)
            elif inputing.startswith("print"):
                args = inputing.split()[1:]
                self.commands["print"](self, args)
            elif inputing == "ls":
                path = os.getcwd()
                self.commands["ls"](self, path)
            elif inputing == "pwd":
                self.commands["pwd"](self)

            elif inputing.startswith("cd"):
                loi = inputing.split()
                path = loi[1]
                try:
                    self.commands["cd"](self, path)
                except FileNotFoundError:
                    print(f"Error: Directory '{path}' not found")
                except PermissionError:
                    print(f"Error: Permission denied to access directory '{path}'")
            elif inputing == "help":
                self.commands["help"](self)
            elif inputing.startswith("mkdir"):
                loi = inputing.split()[1:]
                name = loi[0]
                self.commands["mkdir"](self, name)
            elif inputing.startswith("rmdir"):
                loi = inputing.split()[1:]
                name = loi[0]
                try:
                    self.commands["rmdir"](self, name) 
                except FileNotFoundError:
                    print("That directory does not exist")
            elif inputing.startswith("touch"):
                loi = inputing.split()[1:]
                name = loi[0]
                self.commands["touch"](self, name)
            elif inputing.startswith("rm"):
                loi = inputing.split()[1:]
                name = loi[0]
                self.commands["rm"](self, name)

if __name__ == "__main__": # running the shell 
    shell = Shell()
    shell.run()


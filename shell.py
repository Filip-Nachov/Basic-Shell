import os
import subprocess

class Shell_commands:
    def exit_cmd(self):
        print("Ending shell session")
        exit(0)

    def echo_cmd(self, args):
        print(" ".join(args))

    def print_cmd(self, args):
        print(" ".join(args))


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

    def help_cmd(self):
        print("exit: exits the shell")
        print("pwd: shows your current path")
        print("cd: changes the current directory")
        print("ls: shows all the items in the current directory")
        print("echo or print <word/sentence>: prints out the word or sentences said")


class Shell:
    def __init__(self):
        self.commands = {}
        shell_commands = Shell_commands
        self.commands["exit"] = shell_commands.exit_cmd
        self.commands["echo"] = shell_commands.echo_cmd
        self.commands["print"] = shell_commands.print_cmd
        self.commands["ls"] = shell_commands.ls_cmd
        self.commands["pwd"] = shell_commands.pwd_cmd
        self.commands["cd"] = shell_commands.cd_cmd 
        self.commands["help"] = shell_commands.help_cmd

    def run(self):
        print('For all available commands type "help"')
        while True:
            path = os.getcwd()
            inputing = input(f"$ {path}: ")
            if inputing == "exit":
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
              
if __name__ == "__main__":
    shell = Shell()
    shell.run()


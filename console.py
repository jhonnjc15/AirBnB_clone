#!/usr/bin/python3
"""Define HBNBCommand Class"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Command Interpreter"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return(True)

    def help_quit(self):
        """Help for quit command"""
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """EOF quit the signal"""
        print("")
        return(True)

    def emptyline(self):
        """Do nothing when receiving an empty line"""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()

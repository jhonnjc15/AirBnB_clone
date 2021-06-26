#!/usr/bin/python3
"""Define HBNBCommand Class"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


def parse(arg):
    """Return an argument tuple"""
    return(tuple(arg.split()))

class HBNBCommand(cmd.Cmd):
    """Command Interpreter"""

    prompt = "(hbnb) "
    __classes = {"BaseModel"}

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return(True)

    def help_quit(self):
        """Help for quit command"""
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """EOF signal to quit the program"""
        print("")
        return(True)

    def emptyline(self):
        """Do nothing when receiving an empty line"""
        pass

    def do_create(self, arg):
        """Usage: create <class>
        Create a class instance and print its id"""
        tuparg = parse(arg)
        if len(tuparg) == 0:
            print("** class name missing **")
        elif tuparg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(BaseModel().id)
            storage.save()

    def do_show(self, arg):
        """Usage: show <class> <id>
        Prints the string representation of an instance based on the
        class name and id"""
        tuparg = parse(arg)
        dicObj = storage.all()
        if len(tuparg) == 0:
            print("** class name missing **")
        elif tuparg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(tuparg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(tuparg[0], tuparg[1]) not in dicObj:
            print("** no instance found **")
        else:
            print(dicOBJ["{}.{}".format(tuparg[0], tuparg[1])])


if __name__ == "__main__":
    HBNBCommand().cmdloop()

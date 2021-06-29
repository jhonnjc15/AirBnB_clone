#!/usr/bin/python3
"""Define HBNBCommand Class"""
import cmd
from shlex import split
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import re


def parse(arg):
    """Return an argument tuple"""
    return(tuple(arg.split()))


class HBNBCommand(cmd.Cmd):
    """Command Interpreter"""

    prompt = "(hbnb) "
    __classes = {"BaseModel", "User", "State", "City", "Place", "Amenity",
                 "Review"}

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
            print(dicObj["{}.{}".format(tuparg[0], tuparg[1])])

    def do_destroy(self, arg):
        """Usage: destroy <class> <id>
        Deletes an instance based on the class name and id"""
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
            del dicObj["{}.{}".format(tuparg[0], tuparg[1])]
            storage.save()

    def do_all(self, arg):
        """Usage: all or all <class>
        Prints all string representation of all instances based
        or not on the class name"""
        tuparg = parse(arg)
        if len(tuparg) > 0 and tuparg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            l = []
            for val in storage.all().values():
                if len(tuparg) > 0 and tuparg[0] == val.__class__.__name__:
                    l.append(val.__str__())
                elif len(tuparg) == 0:
                    l.append(val.__str__())
            print(l)

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value>
        Updates an instance based on the class name and id by adding
        or updating attribute"""
        tuparg = split(arg)
        dicObj = storage.all()

        if len(tuparg) == 0:
            print("** class name missing **")
        elif tuparg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(tuparg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(tuparg[0], tuparg[1]) not in dicObj:
            print("** no instance found **")
        elif len(tuparg) == 2:
            print("** attribute name missing **")
        elif len(tuparg) == 3:
            print("** value missing **")
        else:
            obj = dicObj["{}.{}".format(tuparg[0], tuparg[1])]
            if tuparg[2] in obj.__class__.__dict__.keys():
                typeval = type(obj.__class__.__dict__[tuparg[2]])
                obj.__dict__[tuparg[2]] = typeval(tuparg[3])
            else:
                obj.__dict__[tuparg[2]] = tuparg[3]
            storage.save()

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        dic = {"all": self.do_all}
        m = re.search(r"\.", arg)
        if m is not None:
            listarg = [arg[:m.span()[0]], arg[m.span()[1]:]]
            m = re.search(r"\((.*)\)", listarg[1])
            if m is not None:
                c = [listarg[1][:m.span()[0]], m.group()[1:-1]]
                if c[0] in dic.keys():
                    line = "{} {}".format(listarg[0], c[1])
                    return(dic[c[0]](line))
        print("*** Unknown syntax: {}".format(arg))
        return False

if __name__ == "__main__":
    HBNBCommand().cmdloop()

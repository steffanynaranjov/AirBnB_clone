#!/usr/bin/python3
"""
The cmd module is mainly useful for building custom shells
that let a user work with a program interactively.
console.py is the entry point command line interpreter for Airbhb project
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """ entry point of the command interpreter """
    prompt = '(hbnb) '

    air_classes = {"BaseModel": BaseModel, "User": User, "State": State,
                   "City": City, "Amenity": Amenity, "Place": Place,
                   "Review": Review}

    def do_EOF(self, line):
        """EOF to exit the program """
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """ method called when an empty line is entered in
        response to the prompt.
        onecmd(str): Interpret the argument as though it had been
                     typed in response to the prompt.
        onecmd help us to implement an empty line + ENTER
        shouldnt execute anything
        """
        pass

    def do_create(self, arg):
        """ Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id.
        Args:
            arg(str): given class in the command line interpreter
        If the class name is missing, print ** class name missing **
        If the class name doesnt exist, print ** class doesn't exist **
        """
        if not arg:
            print("** class name missing **")
        elif arg not in air_classes.keys():
            print("** class doesn't exist **")
        else:
            instance = air_classes[arg]()
            instance.save()
            print(instance.id)

    def do_show(self, line):
        """
        String representation of a id instance
        """
        if line is None or line == "":
            print("** class name missing **")
        elif line.split(" ")[0] not in HBNBCommand.air_classes:
            print("** class doesn't exist **")
        elif len(line.split(" ")) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(line.split(" ")[0], line.split(" ")[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])


if __name__ == '__main__':
    HBNBCommand().cmdloop()

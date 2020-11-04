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


air_classes = {"BaseModel": BaseModel, "User": User, "State": State,
               "City": City, "Amenity": Amenity, "Place": Place,
               "Review": Review}


class HBNBCommand(cmd.Cmd):
    """ entry point of the command interpreter """
    prompt = '(hbnb) '

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

    def create(self, arg):
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()

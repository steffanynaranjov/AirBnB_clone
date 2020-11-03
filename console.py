#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
import models

""" The cmd module is mainly useful for building custom shells
that let a user work with a program interactively. """


class HBNBCommand(cmd.Cmd):
    """ entry point of the command interpreter """
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """EOF to exit the program """
        return True

    def do_quit(self, arg):
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
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd('\n')

if __name__ == '__main__':
    HBNBCommand().cmdloop()

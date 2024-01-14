#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import json
import models
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    classes = ["BaseModel"]  # Add other model classes here

    def do_create(self, arg):
        """Creates a new instance of BaseModel and saves it to the JSON file"""
        if not arg:
            print("** class name missing **")
            return
        if arg not in self.classes:
            print("** class doesn't exist **")
            return
        new_instance = models.storage.create(arg)
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        all_instances = models.storage.all()
        if key not in all_instances:
            print("** no instance found **")
            return
        print(all_instances[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        all_instances = models.storage.all()
        if key not in all_instances:
            print("** no instance found **")
            return
        del all_instances[key]
        models.storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name"""
        if arg and arg not in self.classes:
            print("** class doesn't exist **")
            return
        all_instances = models.storage.all()
        if not arg:
            print([str(v) for v in all_instances.values()])
        else:
            print([str(v) for v in all_instances.values() if v.__class__.__name__ == arg])

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        all_instances = models.storage.all()
        if key not in all_instances:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        setattr(all_instances[key], args[2], args[3])
        models.storage.save()

    def default(self, line):
        """Called on an input line when the command prefix is not recognized"""
        print("*** Unknown syntax: {}".format(line))

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_EOF(self, arg):
        """Exit the program"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()

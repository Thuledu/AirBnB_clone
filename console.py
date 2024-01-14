#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import json
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_create(self, arg):
        """Creates a new instance of a specified class and saves it to the JSON file"""
        if not arg:
            print("** class name missing **")
            return
        class_name = arg.split()[0]
        if class_name not in ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return
        new_instance = eval(class_name)()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        if args[0] not in ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        all_instances = storage.all()
        if key in all_instances:
            print(all_instances[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        if args[0] not in ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        all_instances = storage.all()
        if key in all_instances:
            del all_instances[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representations of instances based on the class name"""
        class_name = arg.split()[0]
        all_instances = storage.all()
        if class_name in ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]:
            instance_list = [str(obj) for key, obj in all_instances.items() if class_name in key]
            print(instance_list)
        elif not arg:
            print([str(obj) for key, obj in all_instances.items()])
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        if args[0] not in ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        key = args[0] + "." + args[1]
        all_instances = storage.all()
        if key in all_instances:
            setattr(all_instances[key], args[2], args[3])
            storage.save()
        else:
            print("** no instance found **")

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

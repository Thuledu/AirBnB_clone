#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import json
import models
from models import storage
from models.base_model import BaseModel
from models.user import User

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_create(self, arg):
        """Creates a new instance of User and saves it to the JSON file"""
        if arg == "User":
            new_user = User()
            new_user.save()
            print(new_user.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        if args[0] != "User":
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "User." + args[1]
        all_users = storage.all()
        if key in all_users:
            print(all_users[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        if args[0] != "User":
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "User." + args[1]
        all_users = storage.all()
        if key in all_users:
            del all_users[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name"""
        all_users = storage.all()
        user_list = [str(user) for key, user in all_users.items() if 'User' in key]
        print(user_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        if args[0] != "User":
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
        key = "User." + args[1]
        all_users = storage.all()
        if key in all_users:
            setattr(all_users[key], args[2], args[3])
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

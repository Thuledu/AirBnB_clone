#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import re
from shlex import split
from models import storage

def parse(arg):
    curly_braces = re.findall(r"{(.*?)}", arg)
    brackets = re.findall(r"\[(.*?)\]", arg)
    
    if not curly_braces and not brackets:
        return [i.strip(",") for i in arg.split()]
    else:
        tokens = []
        start = 0
        for match in re.finditer(r"[\[\{]", arg):
            tokens.extend([i.strip(",") for i in arg[start:match.start()].split()])
            start = match.end()
            if match.group() == '[':
                end = arg.find(']', start)
                tokens.append(arg[start:end+1])
                start = end + 1
            else:
                end = arg.find('}', start)
                tokens.append(arg[start:end+1])
                start = end + 1
        tokens.extend([i.strip(",") for i in arg[start:].split()])
        return tokens

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def default(self, arg):
        """Default behavior for cmd when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
            }

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

    def do_count(self, arg):
        """Retrieves the number of instances of a class"""
        class_name = arg.split()[0]
        all_instances = storage.all()
        count = sum(1 for key in all_instances if class_name in key)
        print(count)

    def do_show_id(self, arg):
        """Retrieves an instance based on its ID"""
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        if args[0] not in ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]:
            if len(args) < 2:
                print("** instance id missing **")
                return
            key = args[1]
            all_instances = storage.all()
            for k, v in all_instances.items():
                if k.split('.')[1] == key and k.split('.')[0] == args[0]:
                    print(v)
                    return
            print("** no instance found **")

    def do_destroy_id(self, arg):
        """Destroys an instance based on its ID"""
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

    def do_update_id(self, arg):
        """Updates an instance based on its ID with attribute name and value"""
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

    def do_update_dict(self, arg):
        """Updates an instance based on its ID with a dictionary representation"""
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
            print("** dictionary missing **")
            return
        key = args[0] + "." + args[1]
        all_instances = storage.all()
        if key in all_instances:
            obj = all_instances[key]
            if len(args) >= 3:
                try:
                    dictionary = eval(args[2])
                    for k, v in dictionary.items():
                        setattr(obj, k, v)
                    storage.save()
                except:
                    pass
        else:
            print("** no instance found **")

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_EOF(self, arg):
        """Exit the program"""
        print("")
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()

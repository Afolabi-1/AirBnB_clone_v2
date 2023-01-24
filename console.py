#!/usr/bin/python3
'''console file'''
import cmd
from models import storage
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    '''Class HBNB Command'''
    prompt = "(hbnb) "
    class_dic = [
                    "BaseModel",
                    "User",
                    "Place",
                    "State",
                    "City",
                    "Amenity",
                    "Review"
    ]

    def emptyline(self):
        '''emptyline'''
        pass

    def do_quit(self, line):
        '''quit'''
        return True

    def do_EOF(self, line):
        '''EOF'''
        return True

    def do_create(self, line):
        '''create new instance'''
        try:
            if line:
                ClassName = line.split(" ")[0]
                new_dict = eval(ClassName+"()")
                new_dict.save()
                print(new_dict.id)
            else:
                raise SyntaxError
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, line):
        '''show instances'''
        try:
            if line:
                arg_line = line.split(" ")
                ClassName = arg_line[0]
                if ClassName in self.class_dic:
                    if len(arg_line) > 1:
                        current_id = arg_line[1]
                        all_objs = storage.all()
                        full_id = "{}.{}".format(ClassName, current_id)
                        if full_id in all_objs:
                            print(all_objs[full_id])
                        else:
                            raise KeyError
                    else:
                        raise IndexError
                else:
                    raise NameError
            else:
                raise SyntaxError
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, line):
        '''show instances'''
        try:
            if line:
                arg_line = line.split(" ")
                ClassName = arg_line[0]
                if ClassName in self.class_dic:
                    if len(arg_line) > 1:
                        current_id = arg_line[1]
                        all_objs = storage.all()
                        full_id = "{}.{}".format(ClassName, current_id)
                        if full_id in all_objs:
                            del all_objs[full_id]
                            storage.save()
                        else:
                            raise KeyError
                    else:
                        raise IndexError
                else:
                    raise NameError
            else:
                raise SyntaxError
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_all(self, line):
        '''All'''
        loader = storage.all()
        global_list = []
        if line:
            try:
                Model_name = line.split(" ")[0]
                if Model_name in self.class_dic:
                    for cont in loader:
                        if cont.split(".")[0] == Model_name:
                            global_list.append(str(loader[cont]))
                    print(global_list)
                else:
                    raise NameError
            except NameError:
                print("** class doesn't exist **")
        else:
            for cont in loader:
                global_list.append(str(loader[cont]))
            print(global_list)

    def do_update(self, line):
        '''update an instance'''
        try:
            if line:
                arg_line = line.split(" ")
                ClassName = arg_line[0]
                if ClassName in self.class_dic:
                    if len(arg_line) > 1:
                        current_id = arg_line[1]
                        full_id = "{}.{}".format(ClassName, current_id)
                        all_objs = storage.all()
                        if full_id in all_objs:
                            if len(arg_line) > 2:
                                if len(arg_line) > 3:
                                    attribute_name = arg_line[2]
                                    attribute_value = arg_line[3]
                                    try:
                                        all_objs[
                                                    full_id
                                        ].__dict__[
                                                    attribute_name
                                        ] = eval(attribute_value)
                                    except Exception:
                                        all_objs[
                                                    full_id
                                        ].__dict__[
                                                    attribute_name
                                        ] = attribute_value
                                        all_objs[full_id].save()
                                else:
                                    raise ValueError
                            else:
                                raise AttributeError
                        else:
                            raise KeyError
                    else:
                        raise IndexError
                else:
                    raise NameError
            else:
                raise SyntaxError
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")
        except AttributeError:
            print("** attribute name missing **")
        except ValueError:
            print("** value missing **")

    def help_quit(self):
        '''HELP_quit'''
        print("Quit command to exit the program\n")

    def help_EOF(self):
        '''HELP_EOF'''
        print("Ctrl+D command to exit the program\n")

    def help_create(self):
        '''HELP_CREATE'''
        print(
                "Create Command to create a new instance of <Model_name>\
                \nExample:\
                \n> create <Model_name>\
                \n"
        )

    def help_show(self):
        '''HELP_SHOW'''
        print(
                "Show Command to prints the string representation of an\
                \ninstance based on the <Model_name> and <id>\
                \nExample:\
                \n> show <Model_name> <id>\
                \n"
        )

    def help_destroy(self):
        '''HELP_DESTROY'''
        print(
                "Destroy Command to deletes an instance and save changes\
                \nbased on the <Model_name> and <id>\
                \nExample:\
                \n> destroy <Model_name> <id>\
                \n"
        )

    def help_all(self):
        '''HELP_ALL'''
        print(
                "All Command to Prints all string representation of all\
                \ninstances based or not on the <Model_name>.\
                \nExample:\
                \n> all\
                \n\tto print all models\
                \n> all <Model_name>\
                \n\tto print all <Model_name>\
                \n"
        )

    def help_update(self):
        '''HELP_UPDATE'''
        print(
                "Update Command t Updates an instance based on the <Model_name>\
                \nand <id> by adding or updating attribute.\
                \nExample:\
                \n> update <Model_name> <id> <attribute name> <value>\
                \n"
        )

if __name__ == '__main__':
    HBNBCommand().cmdloop()

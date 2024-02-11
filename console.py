#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models import storage
import json
from datetime import datetime
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb)"

    def do_quit(self, content):
        """Exit the prompt."""
        return (True)

    def do_EOF(self, content):
        """Exit the prompt. using ctrl + d """
        return (True)

    def do_create(self, content):
        '''
        - Creates a new instance of class .

            - Usage => create [className]
        '''
        ln = len(content)

        if ln == 0:
            print("** class name missing **")
        elif content not in globals():
            print("** class doesn't exist **")
        else:
            instance = globals()[content]()
            instance.save()
            instance_id = instance.id
            print(instance_id)

    def do_show(self, content):
        """
        - Display instance based on the class name and id .

            - Usage =>  show [className] [id]
        """

        ln = len(content)
        lis = content.split(" ")
        lis_ln = len(lis)

        if ln == 0:
            print("** class name missing **")
        elif lis[0] not in globals():
            print("** class doesn't exist **")
        elif lis_ln == 1:
            print("** instance id missing **")
        else:
            json_dict = storage.all()
            key = "{:s}.{:s}".format(lis[0], lis[1])

            x = False
            for i in json_dict.keys():
                if i == key:
                    x = True
                    break

            if x == True:
                value = json_dict[key]
                full_format = "[{:s}] ({:s}) {:s}".format(lis[0], lis[1], str(value))
                print(full_format)
            else:
                print("** no instance found **")

    def do_destroy(self, content):
        '''
        - Deletes an instance based on the class name and id .

            - Usage => destroy [className] [id]
        '''

        lis = content.split(" ")
        ln = len(content)
        lis_ln = len(lis)
        bol = None

        if ln == 0:
            print("class name missing")
        elif lis[0] not in globals():
            print("** class doesn't exist **")
        elif lis_ln == 1:
            print("** instance id missing **")
        else:
            json_dict = storage.all()
            key_form = "{:s}.{:s}".format(lis[0], lis[1])

            for i in json_dict.keys():
                if key_form == i:
                    del json_dict[key_form]

                    with open("file.json", "w") as f:
                        json.dump(json_dict, f, indent=2)

                    bol = True
                    break
            if bol != True:
                print("** no instance found **")

    def do_all(self, content):
        '''
        - display all instances based on class name or not 

            - Usage => all [className] or all
        '''

        lis = content.split(" ")
        ln = len(content)
        lis_ln = len(lis)
        bol = None

        if ln == 0:
            bol = True
        elif lis[0] not in globals() or lis_ln > 1:
            print("** class doesn't exist **")
        else:
            bol = True

        if bol == True:
            all_dict = storage.all()
            all_dict_lis = []
            for i in all_dict.keys():
                sp = i.split(".")
                x = self.formating(all_dict[i])
                form_full = "[{:s}] ({:s}) {:s}".format(sp[0], sp[1], str(x))
                print(form_full)

    def do_update(self, content):
        '''
        - Updates an instance based on the class name and id by adding or updating attribute

            - Usage => update <class name> <id> <attribute name> "<attribute value>"
        '''

        lis = content.split(" ")
        ln = len(content)
        lis_ln = len(lis)

        not_allowed = ["id", "created_at", "updated_at"]
        bol = 0

        if lis_ln > 4:
            print("!! to many argument")
            return
        elif lis_ln < 4:
            print("!! less argument")
            return

        if ln == 0:
            print("** class name missing **")
        elif lis[0] not in globals():
            print("** class doesn't exist **")
        elif lis_ln == 1:
            print("** instance id missing **")
        elif self.id_checker(lis[1]) == 0:
            print("** no instance found **")
        elif lis_ln == 2:
            print("** attribute name missing **")
        elif lis_ln == 3:
            print("** value missing **")
        elif lis[2] not in not_allowed:  # !! update to searching on classe attrebuit not json file
            dic = storage.all()

            if lis[0] == User.__name__:  # ? User
                attrbutes = [x for x in User.__dict__ if not x.startswith('__')]
            elif lis[0] == BaseModel.__name__:  # ? BaseModel
                attrbutes = [x for x in BaseModel.__dict__ if not x.startswith('__')]
            elif lis[0] == State.__name__:  # ? State
                attrbutes = [x for x in State.__dict__ if not x.startswith('__')]
            elif lis[0] == City.__name__:  # ? City
                attrbutes = [x for x in City.__dict__ if not x.startswith('__')]
            elif lis[0] == Amenity.__name__:  # ? Amenity
                attrbutes = [x for x in Amenity.__dict__ if not x.startswith('__')]
            elif lis[0] == Place.__name__:  # ? Place
                attrbutes = [x for x in Place.__dict__ if not x.startswith('__')]
            elif lis[0] == Review.__name__:  # ? Place
                attrbutes = [x for x in Review.__dict__ if not x.startswith('__')]

            for x in dic.keys():
                if lis[1] == dic[x]["id"]:
                    user_dic = dic[x]
                    for x2 in attrbutes:

                        if lis[2] == x2:
                            #! castinggggggggg
                            if lis[3].isdigit():
                                user_dic[x2] = int(lis[3])
                            elif type(lis[3]) == str:
                                user_dic[x2] = str(lis[3])
                            elif type(lis[3]) == float:
                                user_dic[x2] = float(lis[3])
                            bol = 1
                            break
                    if bol == 1:
                        break
            if bol == 1:
                with open("file.json", "w") as f:
                    json.dump(dic, f, indent=2)
            else:
                print("** no attribute found **")
        elif lis[2] in not_allowed:
            print("** You do not have the permesions to do this **")

    #! my methods------------------------
    ''' formating the string '''

    def formating(self, g):
        dic = g
        tm_fmt = "%Y-%m-%dT%H:%M:%S.%f"

        parsed_datetime1 = datetime.strptime(dic["created_at"], tm_fmt)
        parsed_datetime2 = datetime.strptime(dic["updated_at"], tm_fmt)

        dic["created_at"] = parsed_datetime1
        dic["updated_at"] = parsed_datetime2

        return (dic)

    def id_checker(self, id_z):
        base_data_json = storage.all()

        for i in base_data_json.keys():
            chk_id = base_data_json[i]["id"]
            if chk_id == id_z:
                return (1)
        return (0)

    def time_to_obgect(self, time_z):

        # Convert the string to a datetime object
        dt_object = datetime.fromisoformat(time_z.replace('T', ' '))

        # Format the datetime object as a string
        formatted_date = repr(dt_object)

        # return the formatted string
        return (formatted_date)

    def full_format(self, dictnery):

        dic = dictnery

        # change create_at and update_at foramt to an opject
        z_create_at = self.time_to_obgect(dic["created_at"])
        z_update_at = self.time_to_obgect(dic["updated_at"])
        dic["created_at"] = z_create_at
        dic["updated_at"] = z_update_at

        #formating

        instance_class_name = dic["__class__"]
        instance_id = dic["id"]
        instance_key_dic = str(dic)
        full_format = "[{:s}] ({:s}) {:s}".format(instance_class_name, instance_id, instance_key_dic)

        return (full_format)



    #! my methods------------------------

    #! Built-in methods in CMD-module----------------

    def emptyline(self):
        pass

    # todo
    def default(self, content):

        lis = content.split(".")
        method = lis[1].split("(")
        lis_len = len(lis)
        bol = 0

        if lis_len == 1:
            print("*** Unknown syntax: {:s}".format(content))
        elif lis[1] == "all()":

            if lis[0] in globals():
                dic = storage.all().copy()
                instance_list = []

                for i in dic.keys():
                    if dic[i]["__class__"] == lis[0]:

                        full_format = self.full_format(dic[i])

                        instance_list += [full_format]
                        bol = 1

                if bol == 1:
                    print(instance_list)
                elif bol == 0:
                    print("*** class not found in json-file: {:s}".format(content))
            else:
                print("*** Unknown classe: {:s}".format(content))
        elif lis[1] == "count()":

            if lis[0] in globals():
                dic = storage.all().copy()
                counting = 0

                for x in dic.keys():
                    if dic[x]["__class__"] == lis[0]:
                        counting = counting + 1
                print(counting)

            else:
                print("*** Unknown classe: {:s}".format(content))
        elif method[0] == "show":

            if lis[0] in globals():
                dic = storage.all().copy()
                method_parameter = method[1].split(")")
                instance_id = method_parameter[0].replace('"', '')
                ruse_dic = None

                for x in dic.keys():
                    if dic[x]["id"] == instance_id and dic[x]["__class__"]:
                        ruse_dic = self.full_format(dic[x])
                        bol = 1
                        break
                
                if bol == 1:
                    print(ruse_dic)
                elif bol == 0:
                    print("** no instance found **")
            else:
                print("*** Unknown classe: {:s}".format(content))
        else:
            print("*** Unknown syntax: {:s}".format(content))

    #! Built-in methods in CMD-module----------------
    #!!!!!!!!!!!!!!!
if __name__ == '__main__':
    HBNBCommand().cmdloop()

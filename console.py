#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models import storage
import json


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb)"

    def do_quit(self, content):
        """Exit the prompt."""
        return True

    def do_EOF(self, content):
        """Exit the prompt. using ctrl + d """
        return True

    def emptyline(self):
        pass

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

        # todo
    def do_all(self, content):
        '''
        - display all instances based on class name or not 

            - Usage => all [className] or all
        '''

        lis = content.split(" ")
        ln = len(content)
        lis_ln = len(lis)
        bol =None

        if ln == 0:
            bol =True
        elif lis[0] not in globals() or lis_ln > 1:
            print("** class doesn't exist **")
        else:
            bol =True

        if bol == True:
            all_dict = storage.all()
            all_dict_lis = []
            for i in all_dict.keys():
                sp = i.split(".")
                form_full = "[{:s}] ({:s}) {:s}".format(sp[0], sp[1],str(all_dict[i]))

            print(form_full)



    #!!!!!!!!!!!!!!!


if __name__ == '__main__':
    HBNBCommand().cmdloop()

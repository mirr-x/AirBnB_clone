#!/usr/bin/python3

import json
import os
# from . import objx
from models.base_model import BaseModel


class FileStorage():
    """ privat attr """
    __file_path = "file.json"
    __objects = {}

    ''' __init__(self) method : 
    > storing attrubuites 
    '''

    def __init__(self):

        self.key_id = None
        self.bs_objet = None

    ''' all(self) method : 
    > returning dict of  > self.__objects <
    '''

    def all(self):
        return FileStorage.__objects

    ''' new(self, obj) method : 
    > @obj is an object name 
      in this method we will get the id of @obj 
      and make it as this format " <obj class name>.id " 
      and add it to self.__objects dict
    '''

    def new(self, obj):
        frmt = "{:s}.{:s}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[frmt] = obj
        self.key_id = frmt
        self.bs_objet = obj

    ''' save(self) method : 
    > serializesing means >> turning object into dict (json-format)
      and store it to a json file
    '''

    def save(self):
        from models.base_model import BaseModel

        FileStorage.__objects[self.key_id] = self.bs_objet.to_dict()

        # self.__objects[x.key_clas] = x.to_dict()

        with open(FileStorage.__file_path, "w") as f:
            json.dump(FileStorage.__objects, f, indent=2)

    ''' reload(self) method :
    > deserializesing means >> turning dict (json-format) into object
      and store objectes into a __objects
    '''

    def reload(self):
        bol = os.path.exists(FileStorage.__file_path)

        if bol:
            with open(FileStorage.__file_path, "r") as x:
                FileStorage.__objects = json.load(x)

    #! XXXXXXXXXXXXXXXX

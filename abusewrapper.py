#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 19:58:01 2018

This wrapper enables the user to call rasa with a string and returns a tag 
as required by our modelling of the persone. Please note the rasa server needs
to be running with the trained model. Also adjust command to your enviroment!

@author: julian
"""
import json
import shlex
from subprocess import Popen, PIPE


def abusewrapper(utterance):
    

    command = "curl -X POST \"localhost:5000/parse\" -d '{\"q\":\""+utterance+"\"}'"

    p = Popen(shlex.split(command), stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err = p.communicate()

    if p.returncode != 0:
        print(err)

    j = json.loads(output.decode("utf-8"))
    label = j["intent"]["name"]
    
    
    #Remove in actual code
    print(j["intent"])
    
    if(label == "offensive"):
        return "OFFENSIVEDETECTED"
    elif(label == "sexual/hate"):
        return "SEXUAL/HATEDETECTED"
    else:
        return None

#Remove in actual code
if(abusewrapper("I want to kill you")):
    print(abusewrapper("Fuck you"))

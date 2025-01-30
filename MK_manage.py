#############################################################
#           After Grad Project by Konnor Mascara
#                IM-assist | File: Manage
# 
# Note: Parts have the code has been influenced by similar 
# projects this may also include similar styles and blocks 
# of code copied from the imported files. This is a side 
# project and should not be taken professionally.
#
# Description: Give buttons purpose.
#
# Done   Name     Description
# ----   ----     ----------- 
# Yes | Setup | Allow buttons to delete/create.
# Yes | API   | Allow for API addition.
#
#############################################################

from openai import OpenAI
import json

#Run file depending on button pressed
class setup():
    def delete():
        #Get key and and delete all assistants
        with open('MK_info.json','r') as json_file:
            info = json.load(json_file)
            gpt = info["gpt"]
            if gpt != "":
                client = OpenAI(api_key=gpt)
                ids = [assistant.id for assistant in client.beta.assistants.list()]
                for id in ids:
                    client.beta.assistants.delete(id)
            json_file.close()

        info['gpt'] = ""
        info['assist'] = ""
        info['thread'] = ""

        #Reset file
        with open('MK_info.json','w') as json_file:
            json.dump(info, json_file, indent=4)
            json_file.close()

    def create(keys):
        #Get APIs from either input or personal file
        if keys == "":
            with open('../MK_keys.json','r') as json_file:
                info = json.load(json_file)
                keys = info["gpt"]
                client = OpenAI(api_key=keys)
                json_file.close()
        else:
            try:
                info = {}
                client = OpenAI(api_key=keys)
            except:
                print("Error") #Print to screen

        #Create new assistant
        assist = client.beta.assistants.create(
            name="IM-assist",
            instructions="Be sarcastic",
            model="gpt-4o-mini"
        )

        info['gpt'] = keys
        info['assist'] = assist.id
        info['thread'] = ""

        #Put api/assistant in json
        with open('MK_info.json','w') as json_file:
            json.dump(info, json_file, indent=4)
            json_file.close()

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
# Yes | Delete | Allow full deletion.
# Yes | Create | Allow full completion.
# Yes | Convo  | Allow new thread creation.
# Yes | MyApi  | Allow a quick add. (Will be removed later.)
#
#############################################################

from openai import OpenAI
import json

#Run file depending on button pressed
class setup():

    #Check if assistant exists
    def info():
        with open('MK_info.json','r') as json_file:
            info = json.load(json_file)
            assist = info["assist"]
            json_file.close()
        if assist == "":
            return False
        return True

    #Get key and and delete all assistants
    def delete():
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

    #Add assistant
    def create(keys):
        #Get APIs from either input or personal file
        if keys == "":
            with open('../MK_keys.json','r') as json_file:
                info = json.load(json_file)
                keys = info["gpt"]
                client = OpenAI(api_key=keys)
                json_file.close()
        else:
            info = {}
            client = OpenAI(api_key=keys)
            
        #Create new assistant
        assist = client.beta.assistants.create(
            name="IM-assist",
            instructions="Be Nice and informative",
            model="gpt-4o-mini"
        )

        info['gpt'] = keys
        info['assist'] = assist.id
        info['thread'] = ""

        #Put api/assistant in json
        with open('MK_info.json','w') as json_file:
            json.dump(info, json_file, indent=4)
            json_file.close()

    #Create new thread
    def convo():
        with open("MK_info.json","r") as info_file:
            info = json.load(info_file)
            gpt = info["gpt"]
            client = OpenAI(api_key=gpt)
            info_file.close()
        threads = client.beta.threads.create()
        with open("MK_info.json","w") as add_file:
            info['thread'] = threads.id
            json.dump(info,add_file,indent=4)
            add_file.close()
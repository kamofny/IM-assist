#############################################################
#           After Grad Project by Konnor Mascara
#                IM-assist | File: FULL CLEAR
# 
# Note: Parts have the code has been influenced by similar 
# projects this may also include similar styles and blocks 
# of code copied from the imported files. This is a side 
# project and should not be taken professionally.
#
# Description: Resets for github release
#
# Done   Name     Description
# ----   ----     ----------- 
# Yes | Delete | Delete assistant
# Yes | Clear  | Clear json file
#
#############################################################

from openai import OpenAI
import json

#Get key and then open client
with open('MK-info.json','r') as json_file:
    info = json.load(json_file)
    gpt = info["gpt"]
    client = OpenAI(api_key=gpt)
    json_file.close()

#Go through Asistants and delete
ids = [assistant.id for assistant in client.beta.assistants.list()]
for id in ids:
    client.beta.assistants.delete(id)

info['gpt'] = ""
info['assist'] = ""
info['thread'] = ""

#Reset file
with open('MK-info.json','w') as json_file:
    json.dump(info, json_file, indent=4)
    json_file.close()
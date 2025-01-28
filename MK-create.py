#############################################################
#           After Grad Project by Konnor Mascara
#                IM-assist | File: FULL CLEAR
# 
# Note: Parts have the code has been influenced by similar 
# projects this may also include similar styles and blocks 
# of code copied from the imported files. This is a side 
# project and should not be taken professionally.
#
# Description: Startup new assistant and saves to json.
#
# Done   Name     Description
# ----   ----     ----------- 
# Yes  | Assist | Creates assistant 
# Yes  | json   | Saves info into file
#
#############################################################

from openai import OpenAI
import json

#Get APIs from personal file
with open('../MK-keys.json','r') as json_file:
    info = json.load(json_file)
    gpt = info["gpt"]
    client = OpenAI(api_key=gpt)
    json_file.close()

#Create new assistant
assist = client.beta.assistants.create(
    name="IM-assist",
    instructions="Be sarcastic",
    model="gpt-4o-mini"
)

info['gpt'] = gpt
info['assist'] = assist.id
info['thread'] = ""

#Put api/assistant in json
with open('MK-info.json','w') as json_file:
    json.dump(info, json_file, indent=4)
    json_file.close()
#############################################################
#           After Grad Project by Konnor Mascara
#                IM-assist | File: Start
# 
# Note: Parts have the code has been influenced by similar 
# projects this may also include similar styles and blocks 
# of code copied from the imported files. This is a side 
# project and should not be taken professionally.
#
# Description: Running AI with voice/text
#
# Done   Name     Description
# ----   ----     ----------- 
# @    | @     | @
#
#############################################################

from RealtimeTTS import TextToAudioStream, GTTSEngine
from openai import OpenAI
import json

class running():
    def response(voice):
        stream = TextToAudioStream(GTTSEngine())

        #Get response
        response = running.run(voice)
        result = response.data[0].content[0].text.value

        #Play and send
        stream.feed(result)
        stream.play_async()
        return result

    #Sends and recieve answers
    def run(voice):
        with open("MK_info.json","r") as info_file:
            info = json.load(info_file)
            gpt = info["gpt"]
            assist = info["assist"]
            thread = info["thread"]
            client = OpenAI(api_key=gpt)
            info_file.close()

        client.beta.threads.messages.create(
            thread_id=thread,
            role="user",
            content=voice
        )

        run = client.beta.threads.runs.create_and_poll(
            thread_id=thread,
            assistant_id=assist
        )

        if run.status != 'completed':
            run = client.beta.threads.runs.submit_tool_outputs_and_poll(
                thread_id = thread,
                run_id = run.id
            )

        messages = client.beta.threads.messages.list(
            thread_id=thread
        )

        return messages
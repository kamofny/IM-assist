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

import MK_screen
from RealtimeTTS import TextToAudioStream, GTTSEngine
from RealtimeSTT import AudioToTextRecorder
from openai import OpenAI
import json

class running():
    def __init__(self):
        super().__init__()
        wake_up = "zoe"
        skip = False
        offs = ["stop","off","cancel"]

        #recorder = AudioToTextRecorder(spinner=False, model="tiny.en", language="en", post_speech_silence_duration =0.1, silero_sensitivity = 0.4)
        stream = TextToAudioStream(GTTSEngine()) #'!' throws errors but still runs
        running.create()

        print("Ready!\n")
        while True:
            voice = input() #recorder.text()
            print("Translation: " + voice)
            #recorder.stop()

            #If skip = true user can turn listener off
            if any(off in voice.lower() for off in offs) and skip:
                skip = False

            #Check for wakeup or skip = true
            elif(wake_up in voice.lower()) or skip:

                print("Thinking...")
                response = running.run(voice)
                result = response.data[0].content[0].text.value
                print("Response: " + result)
                stream.feed(result)
                stream.play_async()
                skip = True if "?" in result else False
            
            #skip = true says its listening, else its not
            if skip: print("Active\n")
            else: print("InActive\n")
            #recorder.start()

    #Creates a new thread on start
    def create():
        with open("MK_info.json","r") as info_file:
            info = json.load(info_file)
            gpt = info["gpt"]
            assist = info["assist"]
            thread = info["thread"]
            client = OpenAI(api_key=gpt)
            info_file.close()
        threads = client.beta.threads.create()
        with open("MK_info.json","w") as add_file:
            info['thread'] = threads.id
            json.dump(info,add_file,indent=4)
            add_file.close()
            thread = threads.id

    #Sends and recieve answers
    def run(voice):
        tool_outputs = []

        with open("MK_info.json","r") as info_file:
            info = json.load(info_file)
            gpt = info["gpt"]
            assist = info["assist"]
            thread = info["thread"]
            client = OpenAI(api_key=gpt)
            info_file.close()

        message = client.beta.threads.messages.create(
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

#temp
if __name__ == "__main__":
    temp = running()
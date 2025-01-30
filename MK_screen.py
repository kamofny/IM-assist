#############################################################
#           After Grad Project by Konnor Mascara
#                IM-assist | File: Screen
# 
# Note: Parts have the code has been influenced by similar 
# projects this may also include similar styles and blocks 
# of code copied from the imported files. This is a side 
# project and should not be taken professionally.
#
# Description: File focused on controlling and building the GUI.
#
# Done   Name     Description
# ----   ----     ----------- 
# Yes | Screen | Have proper screen setup.
# No  | Text   | Allow for text to send. (Simple setup and run)
# No  | Voice  | Allow for voice to send. (allow deactive to put ai to sleep)
# No  | Icon   | Custom icon.
# No  | Help   | When typed help add a help screen to console.
# Yes | Setup  | Get Setup working.
#
#############################################################

import tkinter #Not used
import tkinter.messagebox #Not used
import customtkinter
import MK_manage
import MK_start

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue") 

#For the setup window
class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("IM-Assist by KAM")
        self.after(10, self.lift) #Bring to front

        #Add api key?
        self.api_box= customtkinter.CTkEntry(self, placeholder_text="Enter Api Key")
        self.api_box.grid(row=0, column=0, padx=(20,10), pady=(20,20), sticky="nsew")

        self.setup = customtkinter.CTkButton(self, command=self.create, text="Create Assistant")
        self.setup.grid(row=0, column=1, padx=(10,20), pady=(20,20))

        #Seperation between API/Setup
        self.split = customtkinter.CTkFrame(self, height=10)
        self.split.grid(row=1, column=0, columnspan=2, padx=(20,20), pady=(0,0), sticky="nsew")

        #Setup buttons
        self.clear = customtkinter.CTkButton(self, command=self.delete, text="Clear Assistant")
        self.clear.grid(row=2, column=0, padx=(20,10), pady=(20,20))

        self.ready = customtkinter.CTkButton(self, command=self.start, text="Start Assistant")
        self.ready.grid(row=2, column=1, padx=(10,20), pady=(20,20))

    def delete(self): #Allows to change API key
        MK_manage.setup.delete()
    def create(self): #Allows to add API key
        key = self.api_box.get()
        MK_manage.setup.create(key)
    def start(self): #Allows to start new convo
        MK_manage.setup.convo()

#Main app class
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("IM-Assist by KAM")
        self.geometry(f"{1100}x{580}")
        self.toplevel_window = None

        #Determine if things in grid grows(1) or doesnt (0)
        self.grid_columnconfigure(0, weight=1)  
        self.grid_columnconfigure(1, weight=0)
        self.grid_rowconfigure(1, weight=1)

        #Topbar frame
        self.topbar_frame = customtkinter.CTkFrame(self, height=100)
        self.topbar_frame.grid(row=0, column=0, columnspan=2, padx=(20,20), pady=(20,10), sticky="nsew")
        self.topbar_frame.grid_columnconfigure(1, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.topbar_frame, text="IM-Assist by KAM", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=1, padx=20, pady=(20, 20))

        #Topbar buttons
        self.topbar_button_1 = customtkinter.CTkButton(self.topbar_frame, command=self.setup_event, text="Setup")
        self.topbar_button_1.grid(row=0, column=0, padx=20, pady=20)
        self.topbar_button_2 = customtkinter.CTkButton(self.topbar_frame, command=self.voice_event, text="Voice")
        self.topbar_button_2.grid(row=0, column=2, padx=20, pady=20)
        self.topbar_button_2.configure(state="disabled")#temp

        #Console
        self.textbox = customtkinter.CTkTextbox(self, width=250)
        self.textbox.grid(row=1, column=0, columnspan=2, padx=(20,20), pady=(10,10), sticky="nsew")
        self.textbox.insert("end", "Welcome, This is the console. You first need to setup then either speak/text!\n")
        self.textbox.insert("end", "You will need an API key for this to work. Then put into setup and hit create!\n\n")

        #Text entry
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Enter text to start chatting.")
        self.entry.grid(row=2, column=0, padx=(20,10), pady=(10,20), sticky="nsew")
        
        #Submit text button
        self.main_button_1 = customtkinter.CTkButton(master=self, command=self.text_event, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text="Send MSG")
        self.main_button_1.grid(row=2, column=1, padx=(10, 20), pady=(10, 20), sticky="nsew")

    #Moves from text to voice
    def voice_event(self):
        self.textbox.insert("end","voice event\n\n") #placeholder/temp
        self.textbox.see("end")

    #Send text
    def text_event(self):
        msg = self.entry.get()
        response = MK_start.running.response(msg)
        self.textbox.insert("end",response + "\n\n")
        self.textbox.see("end") #Does not clear entry box

    #Setup window is made/moved to the front
    def setup_event(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow()
            
        else:
            self.toplevel_window.deiconify() #De-Minimize it
            self.toplevel_window.focus() #Bring forward

#This is the main file that will open and start everything
if __name__ == "__main__":
    app = App()
    app.mainloop()

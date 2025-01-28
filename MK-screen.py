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
# No  | Help   | When typed help add a help screen to console
#
#############################################################

import tkinter
import tkinter.messagebox
import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue") 

#For the setup window
class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("IM-Assist by KAM")
        self.after(10, self.lift) #Bring to front

        #Setup buttons
        self.clear = customtkinter.CTkButton(self, command=self.placeholder, text="Clear Assistant")
        self.clear.grid(row=0, column=0, padx=(20,10), pady=(20,10))

        self.create = customtkinter.CTkButton(self, command=self.placeholder, text="Create Assistant")
        self.create.grid(row=0, column=1, padx=(10,20), pady=(20,10))

        #Seperation between API/Setup
        self.split = customtkinter.CTkFrame(self, height=10)
        self.split.grid(row=1, column=0, columnspan=2, padx=(20,20), pady=(10,10), sticky="nsew")

        #Add api key?
        self.api_box= customtkinter.CTkEntry(self, placeholder_text="Enter Api Key")
        self.api_box.grid(row=2, column=0, padx=(20,10), pady=(10,20), sticky="nsew")

        self.api_button = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text="Add Api Key")
        self.api_button.grid(row=2, column=1, padx=(10, 20), pady=(10, 20), sticky="nsew")

    def placeholder(self):
        print("placeholder")

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

        #Console
        self.textbox = customtkinter.CTkTextbox(self, width=250)
        self.textbox.grid(row=1, column=0, columnspan=2, padx=(20,20), pady=(10,10), sticky="nsew")
        self.textbox.insert("end", "Welcome, This is the console. You first need to setup then either speak/text!\n\n")

        #Text entry
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Enter text to start chatting.")
        self.entry.grid(row=2, column=0, padx=(20,10), pady=(10,20), sticky="nsew")
        
        #Submit text button
        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text="Send MSG")
        self.main_button_1.grid(row=2, column=1, padx=(10, 20), pady=(10, 20), sticky="nsew")

    #Moves from text to voice
    def voice_event(self):
        self.textbox.insert("end","Placeholder\n\n")
        self.textbox.see("end")

    #Setup window is made/moved to the front
    def setup_event(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow()
            
        else:
            self.toplevel_window.deiconify() #Deminimize it
            self.toplevel_window.focus() #Bring forward

if __name__ == "__main__":
    app = App()
    app.mainloop()

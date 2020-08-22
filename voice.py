  
import pyttsx3 as pys
import os
print("\n\t \t Welcome To Shubham")

pys.speak("Welcome shubham, I am star, I am here to help you!")
print("\nEnter the operation you want to do.\n")
pys.speak("Enter the operation you want to do.")


while True:
    print("Please Enter your command: ",end='')
	#pys.speak("Please spec)
    choice=input()

    if(("run" in choice) or ("execute" in choice)or("start" in choice)or("open" in choice)or("goto" in choice)or("create" in choice)or("what" in choice)or("launch" in choice)):
        #chrome
        if ("chrome" in choice):
            pys.speak("Opening chrome.")
            os.system("start chrome")
        
        #notepad
        elif ("notepad" in choice):
            pys.speak("Opening notepad.")
            os.system("start notepad")
        
        #paint
        elif ("paint" in choice):
            pys.speak("Opening paint.")
            os.system("start mspaint")
        
        #word
        elif ("word" in choice):
            pys.speak("Opening MS Word.")
            os.system("start WINWORD")

        #excel
        elif ("excel" in choice):
            pys.speak("Opening EXCEL.")
            os.system("start EXCEL")
        
        #Power point
        elif ("point" in choice):
            pys.speak("Opening Power point .")
            os.system("start POWERPNT")

        #calculator
        elif ("calculator" in choice)or ("cal" in choice) or ("calc" in choice):
            pys.speak("Opening calculator.")
            os.system("start calc")

        #date
        elif ("date" in choice):
            os.system("echo %date% ")
            pys.speak("Date is printed on the screen")

        #time
        elif ("time" in choice):
            os.system("echo %time% ")
            pys.speak("time is printed on the screen")

        #settings
        elif("settings" in choice):
            pys.speak("Opening settings")
            os.system("start ms-settings:")

        #media player
        elif(("mediaplayer" in choice)or("media" in choice)):
            pys.speak("Opening mediaplayer")
            os.system("start wmplayer")

        
        #Site
        elif(("site" in choice)):
            pys.speak("Which site you want to launch")
            print("Which site you want to launch: ",end="")
            site = input()
            pys.speak("Opening " + site)
            os.system("start chrome "+site+".com")

        
        #create folder
        elif ("folder" in choice):
            pys.speak("Enter folder name.")
            print("Enter folder name: ",end="")
            fol_name=input()
            pys.speak("creating folder.")
            os.system("mkdir "+ fol_name)

        #create file
        elif ("file" in choice):
            pys.speak("Enter the data.")
            print("Enter the data: ",end="")
            data=input()
            pys.speak("Enter the file name.")
            print("Enter file name: ",end="")
            file_name=input()
            pys.speak("creating file.")
            os.system("echo "+ data +">"+file_name)

        else:
            pys.speak("Sorry, I am not able to understand the command, please try again.")
            print("Sorry, I am not able to understand the command, please try again.")
    

    if (("exit" in choice)):
        break

print("\n\t \t !------------------- ThankYou --------------------!")
pys.speak("see you again!!!")
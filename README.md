# NIX The AI based Voice Assistant

#### This was my attempt to make a voice assistant similar to JARVIS (in iron man movie)

## Built with

<img align="right" alt="Coding" width="400" src="https://cdn.activestate.com/wp-content/uploads/2021/12/python-coding-mistakes.jpg">



## Features
It can do a lot of cool things, some of them being:

- Speak date to know the date
- Speak time to know the time
- If you wanna greet me then speak hey buddy or wake up buddy
- i can open sites but you have to tell me the site name along with the domain
- i you want to know the news then speak buzzing,news or headlines
- i can play songs for you on youtube only you to say is play song_name on youtube (ex:- play dariya on youtube)
- i can make notes and close notes just say make a note to note and close the note 
- i can tell you jokes
- i can give information about your system
- you can ask me about the name of city and i will give you the information about the state,country & etc just say where is country_name
- i can switch windows just say switch window
- i can shutdown your computer or restart it just say shutdown or restart
- i can give live camera access just say cam or camera
- i can play radio of all over the world just say radio
- you see live cyber attacks betweeen the countries just say cyber attacks
- i can scan malware trojans files and you dont have to upload any file i can do it my own just say virus
- you can see your current location just say where am i or current location
- i can take screenshots and show the screenshot just say take screenshot or show me the screenshot
    

## Installation

- First clone the repo
- Navigate to the directory of your project
- Install all the requirements by just hitting ``` pip install -r requirements.txt ```
- Install PyAudio from wheel file by following instructions given [here](https://stackoverflow.com/a/55630212)
- Run the program by ``` Auto.py ```
- Enjoy !!!!

## Code Structure


    ├─ driver
    ├─ NIX                 # Main folder for features 
    │  ├── config          # Contains all secret API Keys
    │  ├── features        # All functionalities of JARVIS 
    │  └── utils           # GUI images
    ├─ __init__.py         # Definition of feature's functions
    ├─ gui.ui              # GUI file (in .ui format)
    ├─ main.py             # main driver program of Jarvis
    ├─ requirements.txt    # all dependencies of the program

- The code structure if pretty simple. The code is completely modularized and is highly customizable
- To add a new feature:
  -  Make a new file in features folder, write the feature's function you want to include
  - Add the function's definition to __init__.py
  - Add the voice commands through which you want to invoke the function

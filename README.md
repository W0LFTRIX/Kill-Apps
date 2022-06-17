# Kill-Apps
This script is used to kill apps by terminal on linux


# Installation
``` 
# Clone the repository
$ git clone https://github.com/Wolftrix2514/Kill-Apps.git

# Change directory to Kill-Apps
$ cd Kill-Apps

# Change permission 
$ chmod +x kill_apps
```

# Usage

``` 
# Optional (Launch the python file for change the program name)
# !!! Important, change the name of the program with rename.py else you will just rename the file name
$ python3 rename.py

# Lauch for the first time the script
# Remplace "kill_apps" by the name you gave it with rename.py
$ ./kill_apps 
```

# Integration into your system
```
# Make a command (fist time)
# Remplace "kill_apps" by the name you gave it with rename.py
$ sudo cp kill_apps /usr/bin/

# Change name of the command
$ sudo rm /usr/bin/ancien_name_of_kill_apps

$ python3 rename.py

$ sudo cp new_name_of_kill_apps /usr/bin/
```
 
 
 That's it :) !!!

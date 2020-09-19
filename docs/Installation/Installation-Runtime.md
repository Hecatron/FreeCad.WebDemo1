# Installation

## Runtime Depends

### Installing FreeCad

Currently I'm testing this under Windows using FreeCad 0.19 installed via chocolatey

  * install chocolatey - https://chocolatey.org/
  * launch the command prompt as an administrator (right click run as administrator)

Run the following
```
choco install freecad --ignore-checksums --pre --params "/NoShortcut"
```

The end result should be an install into C:\Program Files\FreeCAD 0.19\FreeCAD_0.19.22411-Win-Conda_vc14.x-x86_64
This appears to be using python 3.8.5 / Qt 5.12.6 at the time of writing.


### Installing Flask

In order to run a minimal webserver within FreeCad we need to install flask
for the copy of python bundled with FreeCad

  * Go into C:\ProgramData\chocolatey\lib\freecad\tools\FreeCAD_0.19.22411-Win-Conda_vc14.x-x86_64\bin\
  * Launch the python.exe within the freecad install (make sure it's running as administrator)

Next install flask using pip
```
import pip;
pip.main(['install'] + ['flask']);
```

### Installing the WebDemo addon manually

If you want to just see the WebDemo running, then manually copy the FreeCad.WebDemo1 directory (the one containing InitGui.py)
Into the FreeCad addons directory

This should be located

  * Windows - C:\Users\username\AppData\Roaming\FreeCAD\Mod
  * Linux - /home/username/.FreeCAD/Mod/

This should make a WebDemo workbench visible when launching freecad
Or instead you can use the --module-path option when launching freecad
```
freecad.exe --module-path="D:\SomeDirectory\FreeCad.WebDemo1\FreeCad.WebDemo1"
```

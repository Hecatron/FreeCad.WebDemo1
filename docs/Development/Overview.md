# Development Overview

There are two entry points within FreeCad for Addons

  * Init.py - loaded first / used for when FreeCad is used just in console mode
  * InitGui.py - loaded second / used for when we launch FreeCad in full GUI mode

InitGui.py is normally used for setting up a new workbench

## Launching

To load in the module from the source directory when running freecad
```
freecad.exe --module-path="D:\SourceCode\Hecatron\FreeCad.WebDemo1\FreeCad.WebDemo1"
```


TODO launch the serer via run.py

## Links

  * https://forum.freecadweb.org/viewtopic.php?f=10&t=49844 - forum thread
  * https://github.com/Vanuan/FreeCADjs/tree/master/freecad-js - another example of using js within freecad

  * https://github.com/HakanSeven12/Modern-UI - an attempt at modernising the FreeCad UI using QT
  * https://github.com/FreeCAD/FreeCAD-addons - list of all addons within freecad
  * https://wiki.freecadweb.org/Addon - types of Addon
  * https://wiki.freecadweb.org/Module_Creation - Module Creation
  * https://wiki.freecadweb.org/Workbench_creation - Workbench Creation
  * https://wiki.freecadweb.org/External_workbenches - Workbenches
  * https://wiki.freecadweb.org/PySide - PySide to PySide2 mappings for Qt5
  * https://translate.google.com/translate?hl=en&sl=de&u=https://forum.freecadweb.org/viewtopic.php%3Fp%3D372496&prev=search&pto=aue - vscode setup

import FreeCAD
import FreeCADGui
import os
import sys

__title__="TODO"
__author__ = "TODO"
__url__ = "TODO"


def icons_path():
    modpath = os.path.dirname(__file__)
    ret = os.path.join(modpath, 'Resources', 'icons')
    return ret


class WebDemo1(Workbench):
    #Icon = os.path.join(icons_path(), 'Freecad.svg')
    MenuText = 'WebDemo1'
    ToolTip = 'Demo of the use of web components for the UI'

    def GetClassName(self):
        return 'Gui::PythonWorkbench'

    def Initialize(self):
        # TODO
        self.tools1 = ["Tool1", "Tool2", "Tool3"]
        #self.appendToolbar("Tools1", self.tools1)
        self.appendMenu("Tools1", self.tools1)
        Log ("Loading WebDemo1... done\n")

    def Activated(self):
        Msg ("WebDemo1.Activated()\n")

    def Deactivated(self):
        Msg ("WebDemo1.Deactivated()\n")

FreeCADGui.addWorkbench(WebDemo1)

import FreeCAD

if FreeCAD.GuiUp:
    import FreeCADGui
    from PySide import QtGui, QtCore


class _CommandFlaskStart:
    '''Start the flask server'''

    def GetResources(self):
        """Return a dictionary with data that will be used by the button or menu item."""
        return {'Pixmap': 'MyCommand.svg',
                'Accel': "Ctrl+A",
                'MenuText': QtCore.QT_TRANSLATE_NOOP("My_Command", "My Command"),
                'ToolTip': QtCore.QT_TRANSLATE_NOOP("My_Command", "Runs my command in the active document")}

    def Activated(self):
        """Run the following code when the command is activated (button press)."""
        print("Activated")

    def isActive(self):
        """Return True when the command should be active or False when it should be disabled (greyed)."""
        return True


class _CommandFlaskStop:
    '''Stop the flask server'''

    def GetResources(self):
        """Return a dictionary with data that will be used by the button or menu item."""
        return {'Pixmap': 'MyCommand.svg',
                'Accel': "Ctrl+A",
                'MenuText': QtCore.QT_TRANSLATE_NOOP("My_Command", "My Command"),
                'ToolTip': QtCore.QT_TRANSLATE_NOOP("My_Command", "Runs my command in the active document")}

    def Activated(self):
        """Run the following code when the command is activated (button press)."""
        print("Activated")

    def isActive(self):
        """Return True when the command should be active or False when it should be disabled (greyed)."""
        return True


if FreeCAD.GuiUp:
    FreeCADGui.addCommand('WebDemo_FlaskStart', _CommandFlaskStart())
    FreeCADGui.addCommand('WebDemo_FlaskStop', _CommandFlaskStop())

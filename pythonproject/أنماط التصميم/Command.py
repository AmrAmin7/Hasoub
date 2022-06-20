from __future__ import annotations
from abc import ABC , abstractmethod

from typing import List

class Command(ABC):
    def __init__(self,app:Application,editor:Editor):
        self._app =app
        self._editor=editor
        self._backup=None

    #//Make the backup of the editor's state
    def saveBackup(self):
        print("SaveBackup")
        self._backup=self._editor.text

    #// Restore the editor's state
    def undo(self):
        print("Undo")
        self._editor.text=self._backup

    @abstractmethod
    def execute(self):
        pass

    def __str__(self):
        return str(self.__class__)

class CopyCommand(Command):
    def __init__(self,app:Application,editor:Editor):
        super().__init__(app,editor)
    def execute(self):
        print("CopyCommand executed")
        self._app.clipboard=self._editor.getSelection()
        return False

class CutCommand(Command):
    def __init__(self, app: Application, editor : Editor):
        super().__init__(app, editor)

    def execute(self):
        print("CutCommand executed")
        self.saveBackup()
        self._app.clipboard = self._editor.getSelection()
        self._editor.deleteSelection()
        return True

class PasteCommand(Command):
    def __init__(self, app: Application,editor:Editor):
        super().__init__(app,editor)
    def execute(self):
        print("PasteCommand executed")
        self.saveBackup()
        self._editor.replaceSelection(self._app.clipboard)
        return True

class UndoCommand(Command):
    def __init__(self,app:Application,editor:Editor):
        super().__init__(app,editor)

    def execute(self):
        print("UndoCommand executed")
        self._app.executeUndo()
        return False

class CommandHistory:
    def __init__(self):
        # noinspection PyUnresolvedReferences
        self.__history: List[Command]=[]

    def push(self,c : Command):
        print("Push CommandHistory")
        self.__history.append(c)

    def pop(self)->Command:
        print("Pop CommandHistory")
        return self.__history.pop()

class Editor:
    def __init__(self,text):
        self.text =text
    def getSelection(self):
        print("Return a selection text")
        return "selected"
    def deleteSelection(self):
        print("delete a text")
        return "Deleted"
    def replaceSelection(self):
        print("replace a selection text")
        return "selected"

class Button:
    def __init__(self):
        self.command=None

    def setCommand(self,command):
        print("setCommand Button",command)
        self.command=command

class Shortcut:
    def __init__(self):
        self.command =None
        self.key=None

    def setCommandOnKeyPress(self,key,command):
        print("setCommandOnkeyPress",key,"to",command)
        self.command=command
        self.key=key

class Application:
    def __init__(self,clipboard :string,editors:List[Editor],activeEditor:Editor, history: CommandHistory):

        self.clipboard=clipboard
        self.editors=editors
        self.activeEditor=activeEditor
        self.history=history

    def createUI(self):
        copy= CopyCommand(self,self.activeEditor)
        copyButton=Button()
        copyShortcut=Shortcut()
        copyButton.setCommand(copy)
        copyShortcut.setCommandOnKeyPress("Ctrl+c",copy)
        self.executeCommand(copy)

        cut = CutCommand(self, self.activeEditor)
        cutButton = Button()
        cutShortcut = Shortcut()
        cutButton.setCommand(cut)
        cutShortcut.setCommandOnKeyPress("Ctrl+x", cut)
        self.executeCommand(cut)

        paste = PasteCommand(self, self.activeEditor)
        pasteButton = Button()
        pasteShortcut = Shortcut()
        pasteButton.setCommand(paste)
        pasteShortcut.setCommandOnKeyPress("Ctrl+v", paste)
        self.executeCommand(paste)

        undo = UndoCommand(self, self.activeEditor)
        undoButton = Button()
        undoShortcut = Shortcut()
        undoButton.setCommand(undo)
        undoShortcut.setCommandOnKeyPress("Ctrl+z", undo)
        self.executeCommand(undo)

    def executeCommand(self,command):
        if (isinstance(command,UndoCommand)):
            self.executeUndo()
        elif command.execute():
            self.history.push(command)

    def executeUndo(self):
        command= self.history.pop()
        if (command!=None) :
            command.undo()

if __name__ =="__main__":
    editor= Editor("Welcome in the Editor")
    history= CommandHistory()
    application =Application("",[editor],editor,history)
    application.createUI()

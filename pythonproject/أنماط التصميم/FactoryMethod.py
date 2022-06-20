from __future__ import annotations
from abc import ABC, abstractmethod

class Dialog(ABC):
    @abstractmethod
    def create_button (self):
        #شيفرة إفتراضية
        pass

    def dialogRender(self) -> str:
        OKButton= self.create_button()
        result =f"Dialog:{OKButton.render()}"
        return result

class WindowsDialog(Dialog):
    def create_button(self) -> WindowsButton:
        return WindowsButton()

class MacDialog(Dialog):
    def create_button(self) -> MacButton:
        return MacButton()

class LinuxDialog(Dialog):
    def create_button(self) -> LinuxButton:
        return LinuxButton()

class Button(ABC):
    @abstractmethod
    def render(self) -> str:
        pass

class WindowsButton(Button):
    def render(self) -> str:
        return "{Result of the WindowsButton}"

class MacButton(Button):
    def render(self) -> str:
        return "{Result of the MacButton}"

class LinuxButton(Button):
    def render(self) -> str:
        return "{Result of the LinuxButton}"

def client_code (dialog: Dialog) -> None:
    print(f"Client : I'm not aware of the Dialog's class. \n"
          f"{dialog.dialogRender()}", end="")

if __name__ == "__main__":
    print("App: Lunched with the WindowsDialog.")
    client_code(WindowsDialog())
    print("App: Lunched with the MacDialog.")
    client_code(MacDialog())
    print("App: Lunched with the LinuxDialog.")
    client_code(LinuxDialog())


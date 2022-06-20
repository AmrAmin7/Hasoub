from __future__ import annotations
from abc import ABC,abstractmethod

class RemoteControl:
    def __init__(self,device:Device):
        self._device =device

    def togglePower(self):
        if self._device.isEnable():
            self._device.disable()
        else:
            self._device.enable()

    def volumedown(self):
        self._device.setVolume(self._device.getVolume()-10)

    def volumeup(self):
        self._device.setVolume(self._device.getVolume()+10)

    def channeldown(self):
        self._device.setChannel(self._device.setChannel()-1)

    def channelup(self):
        self._device.setChannel(self._device.setChannel()+1)

class AdvancedRemoteControl(RemoteControl):
    def mute(self):
        self._device.setVolume(0)
        print("device muted")

class Device(ABC):
    @abstractmethod
    def isEnable(self):
        pass

    @abstractmethod
    def disable(self):
        pass

    @abstractmethod
    def enable(self):
        pass

    @abstractmethod
    def getValume(self):
        pass

    @abstractmethod
    def setValume(self,percent):
        pass

    @abstractmethod
    def getChannel(self):
        pass

    @abstractmethod
    def setChannel(self,channel):
        pass


class TV(Device):
    @abstractmethod
    def isEnable(self):
        print("From TV,isEnable")
        return True

    @abstractmethod
    def disable(self):
        print("From TV ,disable")

    @abstractmethod
    def enable(self):
        print("From TV,enable")

    @abstractmethod
    def getValume(self):
        return "From TV,Valume"

    @abstractmethod
    def setValume(self, percent):
        print("From TV,setValume")

    @abstractmethod
    def getChannel(self):
        return "From TV, Channel"

    @abstractmethod
    def setChannel(self, channel):
        print("From TV,setChannel")

class Radio(Device):
    @abstractmethod
    def isEnable(self):
        print("From TV,isEnable")
        return True

    @abstractmethod
    def disable(self):
        print("From TV ,disable")

    @abstractmethod
    def enable(self):
        print("From TV,enable")

    @abstractmethod
    def getValume(self):
        return "From TV,Valume"

    @abstractmethod
    def setValume(self, percent):
        print("From TV,setValume")

    @abstractmethod
    def getChannel(self):
        return "From TV, Channel"

    @abstractmethod
    def setChannel(self, channel):
        print("From TV,setChannel")

if __name__ =="__main__":
    tv=TV()
    remote= RemoteControl(tv)
    remote.togglePower()

    radio=Radio()
    remote=AdvancedRemoteControl()
    remote.togglePower()

from abc import ABC,abstractmethod

import data as data


class DataSourse(ABC):
    @abstractmethod
    def writeData(self,data):
        pass

    @abstractmethod
    def readData(self):
        pass

class FileDataSourse(DataSourse):
    def __init__(self,filename):
        self._filename=filename

    def writeData(self,data):
        print("Write\"",data,"\"to the file using FileDataSourse")

    def readData(self):
        print("read data from the file using FileDataSourse")
        return "data"

class DataSourseDecorator(DataSourse):
    def __init__(self,sourse:DataSourse):
        self.__wrappee= sourse
    def writeData(self,data):
        self.__wrappee.writeData(data)
    def readData(self):
        return self.__wrappee.readData()

class EncryptionDecorator(DataSourseDecorator):
    def __init__(self,sourse:DataSourse):
        super().__init__(sourse)
    def writeData(self,data):
        print("Encrypt passed data using EncryptionDecorator")
        super().writeData(data)
    def readData(self):
        result=super().readData(data)
        print("decrypt data using EncryptionDecorator")
        return result

class CompressionDecorator(DataSourseDecorator):
    def __init__(self,sourse:DataSourse):
        super().__init__(sourse)
    def writeData(self,data):
        print("compress passed data using CompressionDecorator")
        super().writeData(data)
    def readData(self):
        result=super().readData(data)
        print("decompress data using CompressionDecorator")
        return result

class Application:
    def UsageExample():
        MeanOfSalaryRecords="Salary is 123$"
        sourse= FileDataSourse("somefile.dat")
        sourse.writeData(MeanOfSalaryRecords)

        sourse= CompressionDecorator(sourse)
        sourse.writeData(MeanOfSalaryRecords)

        sourse= EncryptionDecorator(sourse)
        sourse.writeData(MeanOfSalaryRecords)

if __name__ =="__main__":
    Application.UsageExample()

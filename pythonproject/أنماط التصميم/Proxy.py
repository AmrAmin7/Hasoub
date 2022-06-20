from abc import ABC,abstractmethod

class ThirdPartyYouTubeLib(ABC):
    @abstractmethod
    def listVideos(self):
        pass

    @abstractmethod
    def getVideoInfo(self,id):
        pass
    @abstractmethod
    def downloadVideo(self,id):
        pass

class ThirdPartyYouTubeClass(ThirdPartyYouTubeLib):
    def listVideos(self):
        print("Send API request to YouTube for list of video thumbnails")
        return "Videos listed"

    def getVideoInfo(self,id):
        print("get data about video which id is:",id)
        return id

    def downloadVideo(self,id):
        print("Download a video file from YouTube with id",id)
        return id

class CashedYouTubeClass(ThirdPartyYouTubeLib):
    def __init__(self,service: ThirdPartyYouTubeClass):
        self.__service=service
        self.__listCashe=None
        self.__videoCashe=None

    def listVideos(self):
        if self.__listCashe == None:
            self.__listCashe= self.__service.listVideos()
        return self.__listCashe

    def getVideoInfo(self,id):
        if self.__videoCashe==None:
            self.__videoCashe=self.__service.getVideoInfo(id)
        return self.__videoCashe

    def downloadVideo(self,id):
        # this method doesn't defined
        if (not self.downloadExists(id)):
            self.downloadVideo(id)

    def downloadExists(self,id):
        print("downloading....")
        return True

class YouTubeManger:
    def __init__(self,service:ThirdPartyYouTubeLib):
        self._service=service
    def renderVideoPage(self,id):
        info = self._service.getVideoInfo(id)
        # Render the video page
    def renderListPanel(self):
        list=self._service.listVideos()
        # Render the list of video thumbnails.
    def reactonUserInput(self):
        self.renderVideoPage(1)
        self.renderListPanel()

class Application:
    def init():
        aYouTubeService=ThirdPartyYouTubeClass()
        aYouTubeProxy=CashedYouTubeClass(aYouTubeService)
        manger=YouTubeManger(aYouTubeProxy)
        manger.reactonUserInput()

if __name__ =="__main__":
    Application.init()

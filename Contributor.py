class Contributor(object):
    # def __init__(self) -> None:
    def __init__(self, **kwargs):
        # self.val2 = kwargs.get('val2', "default value")
        # self.username = kwargs.get("username", None)
        # self.validatedClipsBeginning = None
        # self.recordedClipsBeginning = None
        # self.currentRecordedClips = None
        # self.currentValidatedClips = None
        # self.clientHash = None

        self.username = kwargs.get("username", None)
        self.validatedClipsBeginning = kwargs.get("validatedClipsBeginning", None)
        self.recordedClipsBeginning = kwargs.get("recordedClipsBeginning", None)
        self.clientHash = kwargs.get("clientHash", None)
        self.currentRecordedClips = None
        self.currentValidatedClips = None
        self.validatedClipsDelta = None
        self.recordedClipsDelta = None
        self.competitionScore = None

    def populateDeltas(self) -> None:
        self.validatedClipsDelta = self.currentValidatedClips - self.validatedClipsBeginning
        self.recordedClipsDelta = self.currentRecordedClips - self.recordedClipsBeginning

    def populateScore(self) -> None:
        self.competitionScore = (
            0.5*self.validatedClipsDelta) + self.recordedClipsDelta

    def test4(self) -> None:
        # print(self)
        for attr, value in self.__dict__.iteritems():
            yield attr, value
        # for i in vars(self):
        # for i in self.__dict__.iteritems():
        #     print(i)

    def __repr__(self):
        return str(self.__dict__)
        # print("hi")
        # for i in self:
        #     print(i)
    #     return "<Contributor a:%s b:%s>" % (self.a, self.b)

    def __str__(self):
        return str(self.__dict__)
        # return "<Contributor username:%s username:%s>" % (self.username, self.username)
        # return dict(self)
        # for i in self:
        #     print(i)
        # return "tper"
        # self.validatedApiResonseContent = None
        # self.recordedApiResonseContent = None


class Mensch:
    def __init__(self):
        pass

    def test3(self):
        print("ok")


if __name__ == "__main__":
    w = Contributor(username="54696d21", clientHash="0272ed18c2dfde45ceb61d5f0dd34fcb8026d55cb6876339dc3762c45bc58699", validatedClipsBeginning=11, recordedClipsBeginning=12)
    w.test4()
    # # print(f)
    # f = Contributor(username="54696d21")
    # p = Contributor(username="54696d21",
    #                 clientHash="0272ed18c2dfde45ceb61d5f0dd34fcb8026d55cb6876339dc3762c45bc58699", validatedClipsBeginning=11)
    # # f.populateScore()
    # f.test2()
    # f.peter()

    # g = Mensch()
    # g.test3()

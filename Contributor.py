class Contributor:
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
        self.currentRecordedClips = None
        self.currentValidatedClips = None
        self.clientHash = kwargs.get("clientHash", None)


        # self.validatedApiResonseContent = None
        # self.recordedApiResonseContent = None

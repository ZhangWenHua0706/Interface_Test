from constants import truck_constant
class sendSmsCode:
    def __init__(self):
        self.mobile=truck_constant.mobile
    def setLoginCodeType(self):
        self.codeType=truck_constant.LoginCodeType
    def getLoginCodeType(self):
        return self.codeType
    def setRegCodeType(self):
       self.codeType = truck_constant.RegCodeType
    def getRegCodeType(self):
        return self.codeType
    def setModPWDCodeType(self):
        self.codeType = truck_constant.ModPWDCodeType
    def getModPWDCodeType(self):
        return self.codeType


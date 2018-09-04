# -*- coding:utf-8 -*-
import os
import codecs
import configparser

proDir = "D:\Python27\Interface_Test"
configPath = os.path.join(proDir, "config.ini")
class ReadConfig:
    def __init__(self):
        try:
            fd = open(configPath)
        except IOError:
            print "File is not accessible."
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(configPath,encoding="utf-8-sig")

    def get_DbTestHost(self):
        value = self.cf.get("DBConfig", 'DbTestHost')
        return value
    def get_DbTestUser(self):
        value = self.cf.get("DBConfig", 'DbTestUser')
        return value
    def get_DbTestPassword(self):
        value = self.cf.get("DBConfig", 'DbTestPassword')
        return value
    def get_DbTestPort(self):
        value = self.cf.get("DBConfig", 'DbTestPort')
        return value
    def get_DbTestName(self):
        value = self.cf.get("DBConfig", 'DbTestName')
        return value
    def get_DbHost(self):
        value = self.cf.get("DBConfig", 'DbHost')
        return value
    def get_DbUser(self):
        value = self.cf.get("DBConfig", 'DbUser')
        return value
    def get_DbPassword(self):
        value = self.cf.get("DBConfig", 'DbPassword')
        return value
    def get_DbPort(self):
        value = self.cf.get("DBConfig", 'DbPort')
        return value
    def get_DbName(self):
        value = self.cf.get("DBConfig", 'DbName')
        return value
    def get_TruckCasePath(self):
        value = self.cf.get("BaseConfig", 'TruckCasePath')
        return value
    def get_TruckApiTestBaseUrl(self):
        value = self.cf.get("BaseConfig", 'TruckApiTestBaseUrl')
        return value
    def get_TruckApiBaseUrl(self):
        value = self.cf.get("BaseConfig", 'TruckApiBaseUrl')
        return value

if __name__=='__main__':
    cc = ReadConfig()
    print cc.get_CasePath()
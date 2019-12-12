#!/usr/bin/env python3
class int:
    def __init__(self, name, ip):
        self.name = name
        self.ip = ip
        self.inn = list()
        self.out = list()

    def addaclin(self, aclnum):
        self.inn.append(aclnum)

    def addaclout(self, aclnum):
        self.out.append(aclnum)

    def listacls(self):
        for acl in self.inn:
            print("In: ",acl)
        for acl in self.out:
            print("Out: ",acl)

    def listinacls(self):
        tmp = list()
        for acl in self.inn:
            tmp.append(acl)
        return tmp

    def listoutacls(self):
        tmp = list()
        for acl in self.out:
            tmp.append(acl)
        return tmp

    def tostring(self):
        stri = ""
        stri += str(self.name) + " "
        stri += "IP: " + str(self.ip) + " "
        for acl in self.inn:
            stri += "In: " + str(acl) + " "
        for acl in self.out:
            stri += "Out: " + str(acl) + " "
        return stri

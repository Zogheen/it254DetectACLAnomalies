#!/usr/bin/env python3
class int:
    def __init__(self):
        self.inn = list()
        self.out = list()
        print("Initialized new interface")

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

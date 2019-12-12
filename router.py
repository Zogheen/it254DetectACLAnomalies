#!/usr/bin/env python3

import int, acl, router, re
from ciscoconfparse import CiscoConfParse

class router:
    def __init__(self):
        self.interfaces = {}
        self.acls = {}

    def addint(self, name, ip):
        self.interfaces[name] = int.int(name, ip)

    def addacl(self, name, str):
        if not name in self.acls:
            self.acls[name] = []
        self.acls[name].append(acl.acl(text=str))

    def assignacl(self, intname, aclname, inout):
        if inout.lower() == 'in':
            self.interfaces[intname].addaclin(aclname)
        if inout.lower() == 'out':
            self.interfaces[intname].addaclout(aclname)

    def tostring(self):
        stri = ""
        for x in self.interfaces:
            stri += "Int: " + self.interfaces[x].tostring() + "\n"
        for x in self.acls:
            for y in self.acls[x]:
                stri += str(y.tostring()) + "\n"
        return stri

def importrouter(str):
    router1 = router()
    parse = CiscoConfParse(str)
    for i in parse.find_objects(r"^interface\sFastEthernet"):
        name = re.search("interface\s(.+)", i.text).group(1)
        ip = i.re_match_iter_typed(r"ip\saddress\s(.*)", group=1, default='')
        router1.addint(name, ip)
        router1.assignacl(name, i.re_match_iter_typed(r"access-group\s(\d+)\s(\w+)", group=1, default=''),
            i.re_match_iter_typed(r"access-group\s(\d+)\s(\w+)", group=2, default=''))
    for i in parse.find_objects(r"^access-list"):
        router1.addacl(i.re_match_typed(r"access-list\s(\d+)", default=''), i.text)
    return router1

def exception(router1):
    for i in router1.acls:
        for j in range(0,len(router1.acls[i])):
            for k in range(j+1, len(router1.acls[i])):
                if router1.acls[i][k].rule != router1.acls[i][j].rule:
                    if router1.acls[i][k].source.port == router1.acls[i][j].source.port and \
                        router1.acls[i][k].dest.port == router1.acls[i][j].dest.port and \
                        router1.acls[i][k].protocol == router1.acls[i][j].protocol:
                        if router1.acls[i][j].source.encompass(router1.acls[i][k].source) and \
                            router1.acls[i][j].dest.encompass(router1.acls[i][k].dest):
                            print("Shadowing: ", router1.acls[i][k].tostring(), "Shadows", router1.acls[i][j].tostring())
                        elif router1.acls[i][k].source.encompass(router1.acls[i][j].source) and \
                            router1.acls[i][k].dest.encompass(router1.acls[i][j].dest):
                            print("Exception: ", router1.acls[i][k].tostring(), "Encompasses", router1.acls[i][j].tostring())
                else:
                    if router1.acls[i][k].source.port == router1.acls[i][j].source.port and \
                        router1.acls[i][k].dest.port == router1.acls[i][j].dest.port and \
                        router1.acls[i][k].protocol == router1.acls[i][j].protocol:
                        if (router1.acls[i][k].source.encompass(router1.acls[i][j].source) and \
                            router1.acls[i][k].dest.encompass(router1.acls[i][j].dest)) or \
                            (router1.acls[i][j].source.encompass(router1.acls[i][k].source) and \
                            router1.acls[i][j].dest.encompass(router1.acls[i][k].dest)):
                            print("Redundancy: ", router1.acls[i][k].tostring(), "Coincides", router1.acls[i][j].tostring())

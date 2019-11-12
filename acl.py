#!/usr/bin/env python3

import re

class acl:

    def __init__(self, **kwargs):
        self.text = kwargs.get('text', '')
        self.parse(self.text)

    def parse(self, text):
        self.list = re.findall("\s(\S+)", text)
        self.index = 0
        self.group = self.list[self.index]
        self.index +=1
        if self.list[self.index].lower() == 'dynamic':
            index +=2
        if self.list[self.index].lower() == 'timeout':
            index +=2
        self.rule = self.list[self.index]
        self.index +=1
        self.protocol = self.list[self.index]
        self.index +=1
        if self.protocol.lower() == 'icmp':
            if self.list[self.index] == 'any':
                self.source = acl.src('any','any','any')
                self.index+=3
            else:
                self.source = acl.src(self.list[self.index], self.list[self.index+1], 'any')
                self.index+=3
            if self.list[self.index] == 'any':
                self.dest = acl.dst('any','any','any')
                self.index+=3
            else:
                self.dest = acl.dst(self.list[self.index], self.list[self.index+1], 'any')
                self.index+=3
        elif self.protocol.lower() == 'tcp' or self.protocol.lower() == 'udp':
            if self.list[self.index] == 'any':
                self.source = acl.src('any','any','any')
                self.index+=3
            else:
                if self.list[self.index+2] == 'any':
                    if (self.index+3 > len(self.list)-1) or (re.search("^\d+\.\d+\.\d+\.\d+$", self.list[self.index+3])):
                        self.source = acl.src(self.list[self.index],self.list[self.index+1],self.list[self.index+2])
                        self.index+=2
                    else:
                        pass
                elif re.search("^\d+\.\d+\.\d+\.\d+$", self.list[self.index+2]):
                    self.source = acl.src(self.list[self.index],self.list[self.index+1],'any')
                    self.index+=2
                else:
                    self.source = acl.src(self.list[self.index],self.list[self.index+1],self.list[self.index+2])
                    self.index+=3
        else:
            if self.list[self.index]:
                pass
            pass


    def tostring(self):
        return [self.group, self.rule, self.protocol, self.source.tostring(), """self.dest.tostring()"""]


    class src:
        def __init__(self, addr, mask, port):
            self.addr = addr
            self.mask = mask
            self.port = port
        def tostring(self):
            return [self.addr, self.mask, self.port]

    class dst:
        def __init__(self, addr, mask, port):
            self.addr = addr
            self.mask = mask
            self.port = port
        def tostring(self):
            return [self.addr, self.mask, self.port]



        #self.group, self.rule, self.protocol, self.source,  = re.findall("^access-list\s(\S+)\s(\S+)\s(\S+)\s(\S+)\s(\S+)\s(\S+)", text)

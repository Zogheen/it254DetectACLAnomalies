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
            #Source
            if self.list[self.index] == 'any':
                if self.list[self.index+1] == 'eq':
                    self.source = acl.src('any','any',self.list[self.index+2])
                    self.index+=3
                elif self.list[self.index+1] == 'gt':
                    self.source = acl.src('any','any',self.list[self.index+3], self.list[self.index+2])
                    self.index+=3
                elif self.list[self.index+1] == 'lt':
                    self.source = acl.src('any','any',self.list[self.index+3], self.list[self.index+2])
                    self.index+=3
                elif self.list[self.index+1] == 'neq':
                    self.source = acl.src('any','any',self.list[self.index+3], self.list[self.index+2])
                    self.index+=3
                    self.index+=3
                else:
                    self.source = acl.src('any','any','any')
                    self.index+=1
            else:
                if self.list[self.index+2] == 'eq':
                    self.source = acl.src(self.list[self.index],self.list[self.index+1],self.list[self.index+3])
                    self.index+=4
                elif self.list[self.index+2] == 'gt':
                    self.source = acl.src(self.list[self.index],self.list[self.index+1],self.list[self.index+3], self.list[self.index+2])
                    self.index+=4
                elif self.list[self.index+2] == 'lt':
                    self.source = acl.src(self.list[self.index],self.list[self.index+1],self.list[self.index+3], self.list[self.index+2])
                    self.index+=4
                elif self.list[self.index+2] == 'neq':
                    self.source = acl.src(self.list[self.index],self.list[self.index+1],self.list[self.index+3], self.list[self.index+2])
                    self.index+=4
                else:
                    self.source = acl.src(self.list[self.index],self.list[self.index+1],'any')
                    self.index+=2
            #Destination
            if self.list[self.index] == 'any':
                if self.index+1 < len(self.list)-1:
                    if self.list[self.index+1] == 'eq':
                        self.dest = acl.dst('any','any',self.list[self.index+2])
                    elif self.list[self.index+1] == 'gt':
                        self.dest = acl.dst('any','any',self.list[self.index+2],self.list[self.index+1])
                    elif self.list[self.index+1] == 'lt':
                        self.dest = acl.dst('any','any',self.list[self.index+2],self.list[self.index+1])
                    elif self.list[self.index+1] == 'neq':
                        self.dest = acl.dst('any','any',self.list[self.index+2],self.list[self.index+1])
                        self.index+=4
                    else:
                        self.dest = acl.dst('any','any','any')
                        self.index+=1
                else:
                    self.dest = acl.dst('any','any','any')
                    self.index+=1
            else:
                if self.index+3 < len(self.list)-1:
                    if self.list[self.index+1] == 'eq':
                        self.dest = acl.dst(self.list[self.index],self.list[self.index+1],self.list[self.index+3])
                    elif self.list[self.index+1] == 'gt':
                        self.dest = acl.dst(self.list[self.index],self.list[self.index+1],self.list[self.index+3],self.list[self.index+2])
                    elif self.list[self.index+1] == 'lt':
                        self.dest = acl.dst(self.list[self.index],self.list[self.index+1],self.list[self.index+3],self.list[self.index+2])
                    elif self.list[self.index+1] == 'neq':
                        self.dest = acl.dst(self.list[self.index],self.list[self.index+1],self.list[self.index+3],self.list[self.index+2])
                        self.index+=4
                    else:
                        self.dest = acl.dst(self.list[self.index],self.list[self.index+1],'any')
                        self.index+=3
                else:
                    self.dest = acl.dst(self.list[self.index],self.list[self.index+1],'any')
                    self.index+=3

            if self.index < len(self.list)-1:
                if self.list[self.index+1] == 'established':
                    self.established = True
                else:
                    self.established = False
            else:
                self.established = False

        else:
            if self.list[self.index]:
                pass
            pass


    def tostring(self):
        return [self.group, self.rule, self.protocol, self.source.tostring(), self.dest.tostring(), self.established]


    class src:
        def __init__(self, *args):
            self.addr = args[0]
            self.mask = args[1]
            self.port = args[2]
            if (len(args) > 3):
                self.mod = args[4]
        def tostring(self):
            return [self.addr, self.mask, self.port]

    class dst:
        def __init__(self, *args):
            self.addr = args[0]
            self.mask = args[1]
            self.port = args[2]
            if (len(args) > 3):
                self.mod = args[4]
        def tostring(self):
            return [self.addr, self.mask, self.port]



        #self.group, self.rule, self.protocol, self.source,  = re.findall("^access-list\s(\S+)\s(\S+)\s(\S+)\s(\S+)\s(\S+)\s(\S+)", text)

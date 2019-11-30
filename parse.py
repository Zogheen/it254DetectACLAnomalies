#!/usr/bin/env python3

from ciscoconfparse import CiscoConfParse
import int, acl

int = int.int()
int.addaclin(100)
int.addaclout(101)
int.addaclout(102)
int.listacls()



parse = CiscoConfParse('i2_startup-config.cfg')

acls = parse.find_objects(r"^access-list")

acl = acl.acl(text='access-list 100 permit tcp 65.5.5.0 0.0.0.255 65.5.5.0 0.0.0.255 eq www established')

print('access-list 100 permit tcp 65.5.5.0 0.0.0.255 65.5.5.0 0.0.0.255 eq www')
print(acl.tostring())

#allintf = parse.find_objects(r"^interf")

#aclintf = list()

#print(*aclintf)

#for obj in allintf:
#    if obj.re_search_children(r"access-group"):
#        aclintf.append(obj)

#acl = aclintf[0].re_match_iter_typed(r'.+access-group\s(\S+)', default='')
#inout = aclintf[0].re_match_iter_typed(r'.+access-group\s\S+\s(\S+)', default='')

#print(acl, inout)






#for intf in parse.find_objects_w_child('^interface', '^\s+shutdown'):
#    print("Shutdown: " + intf.)

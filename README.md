# it254DetectACLAnomalies
Project to detect ACL anomalies for Eastern Michigan University IT 254 Networking II

# Working Description:
  As of this README update, parse.py is the main file to call the others.
  int.py is an object that stores acl names/numbers.
  acl.py is an object in the process of being able to parse and store Cisco configuration ACLs.

# Dependencies:
  CiscoConfParse - available via pip.

              tmp1 = router1.acls[i][j].source.addr.split(".")
              print(tmp1)
              tmp2 = router1.acls[i][j].dest.addr.split(".")
              print(tmp2)
              tmp3 = router1.acls[i][k].source.addr.split(".")
              print(tmp3)
              tmp4 = router1.acls[i][k].dest.addr.split(".")
              print(tmp4)

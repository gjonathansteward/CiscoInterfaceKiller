from easysnmp import Session  
from easysnmp import exceptions as SNMPexceptions

ip = "1.1.1.1"
session = Session(hostname=ip, community='public', version=2)
interfaces = []

device_interfaces = session.walk('.1.3.6.1.2.1.2.2.1.2')
for inter in device_interfaces:
    if inter.value == "Null0":
        continue
    oid = ".1.3.6.1.2.1.2.2.1.7.{}".format(inter.oid_index)
    interfaces.insert(0,(oid, 2))

session.set(".1.3.6.1.4.1.9.5.1.14.3", 1, snmp_type = int)

try:
    session.set_multiple(interfaces)
except SNMPexceptions.EasySNMPTimeoutError:
    print "killed all interfaces"

#Only seems to work for interfaces that are populated/active(not an issue)


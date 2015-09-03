#!/usr/bin/python

"""
Creating a custom mesh topology which connects all the switches to each other
"""

from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink
import sys

def CustomTopology():

    "Start the creating of our custom topology"

    net = Mininet( controller=Controller , link=TCLink)

    info( '*** Adding controller\n' )
    net.addController( 'c0' )

    info( '*** Adding hosts\n' )

    even = odd = 1
    hosts = []
    switches = []
    evenip='19.2.0.'
    oddip='19.2.1.'

    for entry in range(0, S * H ):
	if entry % 2==0:
	    # Ensuring all the even numbered hosts are part of same subnet
            hosts.append(net.addHost('h'+str(entry + 1), ip=evenip+str(even)+'/24'))
            even+=1
	else:
	    # Ensuring all the odd numbered hosts are part of same subnet
	    hosts.append(net.addHost('h'+str(entry + 1), ip=oddip+str(odd)+'/24'))
	    odd+=1


    info( '*** Adding switch\n' )

    for x in range(0,S):
        switches.append(net.addSwitch('s'+str(x+1)))

    info( '*** Creating links\n' )
    
    bwidth=0
    for x in range(0,S):
	for y in range(0,H):
            net.addLink( hosts[H*x+y], switches[x] , bw=bwidth+1)
	    bwidth=(bwidth+1)%2
            
    for x in range(0,S-1):
        net.addLink(switches[x],switches[x+1],bw=2)

    info( '*** Starting network\n')
    net.start()

    info( '*** Running CLI\n' )
    CLI( net )

    info( '*** Stopping network' )
    net.stop()

if __name__ == '__main__':
    S = int(sys.argv[1]) # Number of switches
    H = int(sys.argv[2]) # Number of hosts per switch => Total x * y hosts
    setLogLevel( 'info' )
    CustomTopology()

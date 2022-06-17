from mininet.link import TCLink, Intf
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Node
from mininet.log import setLogLevel, info
from mininet.cli import CLI
from mininet.node import CPULimitedHost, Controller

import time
import os

#Berlian Muhammad Galin Al Awienoor
#1301204378
#IF-44-10

#Build Topologi
class MyTopo(Topo):
  def __init__(self, **opts):
    Topo.__init__(self, **opts)

    #membuat host
    #menambahkan host A
    hA = self.addHost( 'hA' )
    #menambahkan host B
    hB = self.addHost( 'hB' )

    #membuat router
    #menambahkan router 1
    r1 = self.addHost( 'r1' )
    #menambahkan router 2
    r2 = self.addHost( 'r2' )
    #menambahkan router 3
    r3 = self.addHost( 'r3' )
    #menambahkan router 4
    r4 = self.addHost( 'r4' )
    
        
    #membuat link
    #link host - router
    #menghubungkan hA dengan r1
    self.addLink( 'hA', 'r1', intfName1='hA-eth0', intfName2='r1-eth0', cls=TCLink, bw=1 )
    #menghubungkan hA dengan r2
    self.addLink( 'hA', 'r2', intfName1='hA-eth1', intfName2='r2-eth0', cls=TCLink, bw=1 )
    #menghubungkan hB dengan r3
    self.addLink( 'hB', 'r3', intfName1='hB-eth0', intfName2='r3-eth0', cls=TCLink, bw=1 )
    #menghubungkan hB dengan r4
    self.addLink( 'hB', 'r4', intfName1='hB-eth1', intfName2='r4-eth0', cls=TCLink, bw=1 )

    #link router - router
    #menghubungkan r1 dengan r3
    self.addLink( 'r1', 'r3', intfName1='r1-eth1', intfName2='r3-eth1', cls=TCLink, bw=0.5 )
    #menghubungkan r1 dengan r4
    self.addLink( 'r1', 'r4', intfName1='r1-eth2', intfName2='r4-eth1', cls=TCLink, bw=1 )
    #menghubungkan r2 dengan r3
    self.addLink( 'r2', 'r3', intfName1='r2-eth1', intfName2='r3-eth2', cls=TCLink, bw=1 )
    #menghubungkan r2 dengan r4
    self.addLink( 'r2', 'r4', intfName1='r2-eth2', intfName2='r4-eth2', cls=TCLink, bw=0.5 )



def run():
    os.system('mn -c')
    os.system( 'clear' )
    topo =MyTopo()
    net = Mininet(topo=topo, host=CPULimitedHost, link=TCLink)
    net.start()

    #simpan node topologi pada variabel 
    hA, hB         = net.get( "hA", "hB" )
    r1, r2, r3, r4 = net.get( "r1", "r2", "r3", "r4" )

    r1.cmd("sysctl net.ipv4.ip_forward=1") 
    r2.cmd("sysctl net.ipv4.ip_forward=1")
    r3.cmd("sysctl net.ipv4.ip_forward=1")
    r4.cmd("sysctl net.ipv4.ip_forward=1")

    #konfigurasi IP hA
    hA.cmd( "ifconfig hA-eth0 0" )
    hA.cmd( "ifconfig hA-eth1 0" )
    hA.cmd( "ifconfig hA-eth0 192.168.1.1 netmask 255.255.255.0" )
    hA.cmd( "ifconfig hA-eth1 192.168.8.1 netmask 255.255.255.0" )

    #konfigurasi IP hB
    hB.cmd( "ifconfig hB-eth0 0" )
    hB.cmd( "ifconfig hB-eth1 0" )
    hB.cmd( "ifconfig hB-eth0 192.168.7.2 netmask 255.255.255.0" )
    hB.cmd( "ifconfig hB-eth1 192.168.6.2 netmask 255.255.255.0" )

    #konfigurasi IP r1
    r1.cmd( "ifconfig r1-eth0 0" )
    r1.cmd( "ifconfig r1-eth1 0" )
    r1.cmd( "ifconfig r1-eth2 0" )
    r1.cmd( "ifconfig r1-eth0 192.168.1.2 netmask 255.255.255.0" )
    r1.cmd( "ifconfig r1-eth1 192.168.3.1 netmask 255.255.255.0" )
    r1.cmd( "ifconfig r1-eth2 192.168.4.1 netmask 255.255.255.0" )

    #konfigurasi IP r2
    r2.cmd( "ifconfig r2-eth0 0" )
    r2.cmd( "ifconfig r2-eth1 0" )
    r2.cmd( "ifconfig r2-eth2 0" )
    r2.cmd( "ifconfig r2-eth0 192.168.8.2 netmask 255.255.255.0" )
    r2.cmd( "ifconfig r2-eth1 192.168.5.1 netmask 255.255.255.0" )
    r2.cmd( "ifconfig r2-eth2 192.168.2.1 netmask 255.255.255.0" )

    #konfigurasi IP r3
    r3.cmd( "ifconfig r3-eth0 0" )
    r3.cmd( "ifconfig r3-eth1 0" )
    r3.cmd( "ifconfig r3-eth2 0" )
    r3.cmd( "ifconfig r3-eth0 192.168.7.1 netmask 255.255.255.0" )
    r3.cmd( "ifconfig r3-eth1 192.168.3.2 netmask 255.255.255.0" )
    r3.cmd( "ifconfig r3-eth2 192.168.5.2 netmask 255.255.255.0" )

    #konfigurasi IP r4
    r4.cmd( "ifconfig r4-eth0 0" )
    r4.cmd( "ifconfig r4-eth1 0" )
    r4.cmd( "ifconfig r4-eth2 0" )
    r4.cmd( "ifconfig r4-eth0 192.168.6.1 netmask 255.255.255.0" )
    r4.cmd( "ifconfig r4-eth1 192.168.4.2 netmask 255.255.255.0" )
    r4.cmd( "ifconfig r4-eth2 192.168.2.2 netmask 255.255.255.0" )

    #konfigurasi router
    r1.cmd( "echo 1 > /proc/sys/net/ipv4/ip_forward" )
    r2.cmd( "echo 1 > /proc/sys/net/ipv4/ip_forward" )
    r3.cmd( "echo 1 > /proc/sys/net/ipv4/ip_forward" )
    r4.cmd( "echo 1 > /proc/sys/net/ipv4/ip_forward" )

    #static routing
    #host A
    hA.cmd( "ip rule add from 192.168.1.1 table 1" )
    hA.cmd( "ip rule add from 192.168.8.1 table 2" )

    hA.cmd( "ip route add 192.168.1.0/24 dev hA-eth0 scope link table 1" )
    hA.cmd( "ip route add default via 192.168.1.2 dev hA-eth0 table 1" )

    hA.cmd( "ip route add 192.168.8.0/24 dev hA-eth1 scope link table 2" )
    hA.cmd( "ip route add default via 192.168.8.2 dev hA-eth1 table 2" )

    hA.cmd( "ip route add default scope global nexthop via 192.168.1.2 dev hA-eth0" )
    hA.cmd( "ip route add default scope global nexthop via 192.168.8.2 dev hA-eth1" )
    
    #host B
    hB.cmd( "ip rule add from 192.168.7.2 table 1" )
    hB.cmd( "ip rule add from 192.168.6.2 table 2" )

    hB.cmd( "ip route add 192.168.7.0/24 dev hB-eth0 scope link table 1" )
    hB.cmd( "ip route add default via 192.168.7.1 dev hB-eth0 table 1" )

    hB.cmd( "ip route add 192.168.6.0/24 dev hB-eth1 scope link table 2" )
    hB.cmd( "ip route add default via 192.168.6.1 dev hB-eth1 table 2" )
    
    hB.cmd( "ip route add default scope global nexthop via 192.168.7.1 dev hB-eth0" )
    hB.cmd( "ip route add default scope global nexthop via 192.168.6.1 dev hB-eth1" )

    #menyetting gateaway router
    #router 1
    r1.cmd( "route add -net 192.168.8.0/24 gw 192.168.3.2" )
    r1.cmd( "route add -net 192.168.5.0/24 gw 192.168.3.2" )
    r1.cmd( "route add -net 192.168.2.0/24 gw 192.168.4.2" )
    r1.cmd( "route add -net 192.168.7.0/24 gw 192.168.3.2" )
    r1.cmd( "route add -net 192.168.6.0/24 gw 192.168.4.2" )

    #router 2
    r2.cmd( "route add -net 192.168.1.0/24 gw 192.168.2.2" )
    r2.cmd( "route add -net 192.168.4.0/24 gw 192.168.2.2" )
    r2.cmd( "route add -net 192.168.3.0/24 gw 192.168.5.2" )
    r2.cmd( "route add -net 192.168.7.0/24 gw 192.168.5.2" )
    r2.cmd( "route add -net 192.168.6.0/24 gw 192.168.2.2" )

    #router 3
    r3.cmd( "route add -net 192.168.6.0/24 gw 192.168.3.1" )
    r3.cmd( "route add -net 192.168.4.0/24 gw 192.168.3.1" )
    r3.cmd( "route add -net 192.168.2.0/24 gw 192.168.5.1" )
    r3.cmd( "route add -net 192.168.8.0/24 gw 192.168.5.1" )
    r3.cmd( "route add -net 192.168.1.0/24 gw 192.168.3.1" )

    #router 4
    r4.cmd( "route add -net 192.168.7.0/24 gw 192.168.2.1" )
    r4.cmd( "route add -net 192.168.5.0/24 gw 192.168.2.1" )
    r4.cmd( "route add -net 192.168.3.0/24 gw 192.168.4.1" )
    r4.cmd( "route add -net 192.168.1.0/24 gw 192.168.4.1" )
    r4.cmd( "route add -net 192.168.8.0/24 gw 192.168.2.1" )

	
    time.sleep(1)
    print("\n*** Bandwidth test")
    time.sleep(1)

    #iperf
    hB.cmd('iperf -s &')
    time.sleep(1)

    hA.cmdPrint('iperf -t 60 -c 192.168.6.2 &')
    
    #untuk tes percobaan transfer data buffer 20, 40, 60, 100
    r1.cmdPrint("tc qdisc del dev r1-eth0 root")
    r1.cmdPrint("tc qdisc add dev r1-eth0 root netem delay 100ms")
    
    CLI(net)
    net.stop()

if __name__=='__main__':
    setLogLevel('info')
    run()


- throughput: successful message communication rate (data packets or bits/second)

- bandwidth: maximum possible data transfer rate on a particular communication channel/path
	- throttling: slowing down data transfer to charge premiums for speed or to manage traffic
	- management: preventing network congestion (hitting capacity limits) and other network traffic issues
	- shaping/scheduling: controlling send/receive queue sequencee
	- allocation: dividing signal frequencies into segments designated for agents/applications


- os: Linux knowledge (OS, security, networking, configuration & management)
	
	- os types
		- Network Operating System (NOS): OS designed to support devices (workstations, databases, personal computers) over a network
			- mac, linux, windows
			- processor/multiprocessing support, authentication, web services
	- linux kernel: manages hardware resources, providing an interface for user interaction with hardware resources
	- LILO: a boot loader for Linux, loads the Linux OS into the main memory to begin operations
	- centos, ubuntu, redhat, debian, fedora
	- components:
		- kernel (code depends on architecture/dist)
		- system call interface
		- gnu c library (glibc)
		- accounts
			- root account: system administrator account, giving full control of the system, including creating/maintaining user accounts, assign permissions to accounts, etc
		- shells: interpreters: bash (Bourne Again SHell), csh, ksh, bsh
			- BASH commands are case sensitive
			- DOS commands are not case sensitive, follows a file naming convention
		- GUIs
		- system utilities
		- user applications
		- bootload: LILO
		- memory: swap space, RAM, main memory
		- daemons: extend functionality of OS; services that actively listen for service requests, act upon them, gets disconnected on completion & waits for further requests
	- internal commands: commands built in the shells
	- inode: unique file name by the operating system
	- pid: uniquely identifies each process
	- mount:
		- soft mount: if client fails to connect to server, reports error & closes connection 
		- hard mount: if client fails to connect to server, connection hangs & once system is up again, it retries to connect to server
	- permissions: read/write/execute
	- vi modes: command, insert (i), replace, :wq (exit with save), :q! (exit without save), x (delete current char), dd (delete line)
	- commands
		- at: schedule a command
		- user commands: last, chage, chsh, lsof, chown, chmod, useradd/del, newuser
		- gunzip: unzip gzip files
		- combine commands with ; && 
		- replace text: sed -i 's/old-text/new-text/g' input.txt
		- tar
		- install
			- Debian/Ubuntu users: apt-get install/remove pkg 
			- Red Hat-based distributions: dnf or yum
		- memory
			- cat/proc/meminfo
			- df -h
			- du -a
		- pwd: print working directory
		- mv: rename file
		- terminate process: kill pid
		- # comments
		- () grouping commands

	- rules:
		- filename char limit: 255 characters
		- swap partition size: double physical memory available, minimum size: amount of memory installed
		- locations
			- /etc storage system config files
				- /etc/login.defs (system password config)
			- /usr/local directory contains locally installed files, to store software installed from a source or other third party software
			- parallel ports: include printers, scanners, & other devices attached (/dev/lp0 for LPT1, /dev/lp1 for LPT2)
			- Drives (floppy/hard drives): represented with /dev/fd0 for floppy drive 1, /dev/hda for hard drive 1

	- swap space: specify a space used by Linux to hold a concurrent running program temporarily, when RAM is out of space
	
	- security tools
		- rkhunter (rootkit hunter)
    	- Chkrootkit
    	- ClamAV
    	- LMD (Linux Malware Detect)
    	- Lynis

    - ping: program to test host reachability & if it can accept requests on an IP network, sends ICMP Echo to a network computer on the network & waits for reply

- Networking

    - concepts

    	- protocol components
    		- syntax: format rules
    		- semantics: meaning of bits
    		- timing: when data should be sent/received

    	- RSA: public key for encryption, decryption key is kept private; encryption key created using two large prime numbers & published with auxiliary value, considered relatively slow

    	- Ethernet: 
    		- a network tech used in LAN/MAN/WAN
    		- connects devices using cables for data transmission
    		- provides services on Physical & Data Link layers of the OSI Model

		- Optic fibers advantages:
		    - Greater bandwidth than other metal cables
		    - Low power loss, allows longer transmission distances
		    - immune to electromagnetic interference
		    - Lesser production rates
		   	- Thin and light
		    - difficult to tap

		- IPv6 (Internet Protocol version 6): latest version of the Intenet Protocol with 128 bit IP address length

    	- Round Trip/Delay Time: time between signal send & ACK received
    	- Tunnel mode: encrypts whole IP packet including headers & payload, used in a Site-to-Site VPN to secure communications between security gateways, firewalls, etc.
    	- domain vs. workgroup
		    - Domain	
				- at least one computer acts as a server
				- centralized database
				- Computers can be on different LANs
		    - Workgroup	
				- computers are peers on the same LAN, with each having its own database
    	- piggybacking: 
    		- delaying the ACK during transmission of data packets, and attaching it to the next outgoing data frame
    		- sender sends an ack (control frame) to receiver after receiving data packets
    		- receiver does not send the acknowledgment immediately but waits until for next data packet from network layer
    		- then receiver attaches ACK to outgoing data frame
    	- MAC (Media Access Control) address (physical address)
    		- computer’s unique number assigned by a Network Interface Controller (NIC)
    		- a 48-bit number identifying each device on a network
    		- used as a network address for network communications such as an Ethernet, Wi-Fi
    	- packet: units of information recognized by networking components (can be any information content)
    	- router: 
    		- device that transfers the data packets within a network
    		- connects lan/wan devices, with packet filtering, most complicated
    		- located at network/node intersection or gateways
    		- can be stand-alone/virtual
    	- switch: connects lan devices, with packet filtering
    	- hub: connects ethernet devices, without packet filtering, least complicated
    	- link: connection between devices
    	- node: device that can send/receive data in a network
    	- topology: network node arrangement
			Bus Topology: devices share a common communication line
			Star Topology: nodes connect to central hub device
			Ring Topology: Each node connects to 2 other nodes
			Mesh Topology: Each node connects to at least 1 node
			Tree Topology (Hierarchical Topology): Similar to star topology, inherits the bus topology
			Daisy Chain Topology: All nodes connect linearly
			Hybrid Topology: nodes connect in more than 1 topology styles
			Point-to-Point Topology: connects 2 hosts (computers, servers, etc)
    	- osi (Open Systems Interconnection) model layers
    		    hardware: 
    		        - physical (symbol): transfers raw data bits over physical links
    		    	- data link (data frame): reliable data frame transmission between nodes connected by on physical layer
    		    	- network (packets): structures/manages multiple nodes with addressing/routing/traffic control
			    interim/general: 
			    	- transport (segments/datagrams): reliable data packet transmission between the different network points
			    software (handles data):
			    	- session: manages sessions
			    	- presentation: data transmission between service device & application
			    	- application: specifies shared communication protocols & interface methods
    	- network types
    		- backbone network: connective network
    		- point to point network: physical connection between nodes, between any network device (computer, printer, etc)
    		- LAN (Local Area Network): 
    			- network between devices located in a small physical location
    			- can be wireless/wired
    			- Topology: network node arrangement
   				- Protocol: data transfer rules
    			- Media: devices connection options, like optic fibers, coaxial cables, twisted-pair wires, etc
    		- wireless networks: use waves like radio waves infrared waves and microwaves rather than cables/fibers/wires
    	- firewall
    		- network security system to monitor/control network traffic with predefined rules
    		- establish barriers between the internal/external networks
    	- subnet mask
    		- number describing IP address range usable in a network, to assign subnetworks/subnets, which are LAN’s connected to the internet
			- a 32-bit number which masks the IP address & divides it into two parts:
				- network address
				- host address
			- created by setting network bits to “1”, host bits to “0”s
			- two network addresses that cant be assigned to any host on the network (“0” & “255”, network & broadcast address)

    - protocols: 

    	- SLIP (Serial Line Internet Protocol): allows a user to access internet using modem
    	
    	- DHCP (Dynamic Host Configuration Protocol)
    		- network management protocol on UDP/IP
    		- automatically assigns IP addresses to network devices, reducing need of network admin

    	- ICMP (Internet Control Message Protocol)
    		 - a supporting Internet protocol
    		 - sends error messages & communication success/failure info
    		 - if a service is not available, an error is reported

    	- DNS (Domain Name System): 
    		- naming system for internet devices 
    		- hierarchical/decentralized system translating domain names to numerical IP Addresses required to identify/locate devices

    	- TCP/IP (compressed more reliable horizontal version of OSI, without strict boundaries)
    		Process (Application Layer): HTTP, FTP, Telnet, SMTP, DNS
    	    Transport/Host-to-Host: TCP, UDP
		    Network/Internet Layer: IP
		    Physical/Data Link Layer/Network Access Interface: Ethernet, Token Ring, Outer-link Layer protocols

    	- SSH: public-key cryptography authentication 
    		- ssh -i key.pem user@ip
    		- allows data compression & sending graphical commands via X11
    		- can protect against DNS spoofing & man-in-the-middle attacks

    	- routing protocols
	    	- OSPF (Open Shortest Path First)
	    		- find best path for packets being transmitted over interconnected networks
	    	- RIP (Routing Information Protocol)
	    		- dynamic routing protocol
	    		- uses hop count as its primary metric to find best path between source/destination
	    		- works in application layer
	    		- AD (Administrative Distance): 120
    	- TCP (Transmission Control Protocol)
    		- connection-oriented protocol
    		- establishes/maintains connection between devices before messages are exchanged, until both of them are done exchanging messages
    		- for reliability of message & data segment order/integrity (vs. UDP for speed)
    		- receives ACK (acknowledgment)
    		- used by file transfer & email protocols
    		- determines how app data can be broken down into packets that can be delivered over a network
    		- sends/receives packets to/from network (IP) layer
    		- handles flow control, has congestion control mechanism
    		- resends erroneous segments
    	- UDP (User Datagram Protocol)
    		- creates a low-latency & loss-tolerating communications between applications connected over the internet
    		- enables process-to-process communication
    		- communicates via datagrams/messages
    		- used by DNS, multimedia
    	- HTTP (HyperText Transfer Protocol)
    		- allows internet communication, defines how to transmit/format messages over internet
    		- a TCP/ IP protocol
    		- uses the port number 80/443
    		- connection-less, stateless, not dependent on connecting media
	    - WebSocket
	    	- communications protocol, providing full-duplex (mutual two-way communication in a point-to-point network) communication channels over a single TCP connection
	    	- both websocket & http are located at layer 7 in the OSI model and depend on TCP at layer 4
	    	- compatible with HTTP, handshake uses upgrade header
	    	- lower overhead, allows two-way communication
	    	- not restricted by same origin policy, so has to validate the "Origin" header, using tokens to avoid CSRF possible with cookies/http auth
	    	- usually uses tcp port 443
	    	- unaware of proxy servers and firewalls
	    	- uses HTTP CONNECT method to set up a persistent tunnel
	    - TLS
    	- NAT (Network Address Translation)
    		- handles remapping IP Address spaces by changing IP headers of packets transmitted across traffic routing devices
    	- SMTP: Simple Mail Transfer Protocol
    
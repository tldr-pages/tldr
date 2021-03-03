# Tcpdump
> [useful tcpdump examples](https://www.howtouselinux.com/post/10-useful-tcpdump-command-examples)
### Capture traffic on specific interface ( -i)  

$  tcpdump -i ens160 
$  tcpdump -i any

### Capture ip host-specific packets ( host filter/ip filter )
$  tcpdump -i ens160 -c 5  host 140.240.61.21
### Capture packets on a specific port  ( port)
$  tcpdump -i any port 8000

### Write packets to a file ( -w )
$  tcpdump -c 5 -w network_file_linux.pcap -i any
### Capture packets from a specific protocol  
$  tcpdump -i ens160 -c 5 -nn tcp
### Filter tcpdump packets from specific source & dest host
$  tcpdump src 100.10.8.121
$  tcpdump dst 14.211.62.121

### Rotate tcpdump packets 
$ tcpdump -i ens160 -w /tmp/network-%H-%M.pcap -W 48 -G 300 -C 100
-C file_size (M) -G rotate_seconds -W filecount 

### tcpdump -G 100 -W 3 -w network-%H-%M.pcap port 19096
  1 root  wheel   384881 Feb 13 17:09 network-17-08.pcap
  
  1 root  wheel  2096619 Feb 13 17:11 network-17-09.pcap
  
  1 root  wheel   320744 Feb 13 17:13 network-17-11.pcap

### Capture Multiple hosts with tcpdump
$ tcpdump src 192.168.0.10 or src 192.168.0.10 
### Filter Multiple ports with tcpdump
$ tcpdump -i eth0 port 22 or port 9402 
### Filter Multiple interfaces
$ tcpdump -i any

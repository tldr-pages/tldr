# httpry

> A lightweight packet sniffer for displaying and logging HTTP traffic.
> It can be run in real-time displaying the traffic as it is parsed, or as a daemon process that logs to an output file.
> More information: http://dumpsterventures.com/jason/httpry/.

- Save output to a file:

`httpry -o out.log`

- Listen on a specific interface and save output to a binary pcap format file:

`httpry -i eth0 -b out.pcap`

- Filter output by HTTP method strings:

`httpry -m get,head`

- Read from an input capture file and filter by IP:

`httpry -r out.log 'host 192.168.5.25'`

- Run as daemon process:

`httpry -d -o /var/log/http.log`

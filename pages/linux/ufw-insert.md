# ufw insert

> Insert a firewall rule at a specific numbered position.
> More information: <https://manned.org/ufw>.

- Display numbered firewall rules to find rule positions:

`sudo ufw status numbered`

- Insert an allow rule at a specific numbered position:

`sudo ufw insert {{1}} allow {{port}}`

- Insert a rule allowing a specific protocol on a port at position 1:

`sudo ufw insert 1 allow {{port}}/{{tcp}}`

- Insert a deny rule blocking traffic from an IP address at position 1:

`sudo ufw insert 1 deny from {{ip_address}}`

- Insert an allow rule from a subnet to a specific port and protocol:

`sudo ufw insert {{1}} allow from {{192.168.1.0/24}} to any port {{22}} proto {{tcp}}`

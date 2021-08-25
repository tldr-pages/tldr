# ipset

> A tool to create IP sets for firewall rules.
> More information: <https://manned.org/ipset>.

- Create an empty IP set which will contain IP addresses:

`ipset create {{set_name}} hash:ip`

- Destroy an ip set named `test_set`:

`ipset destroy {{test_set}}`

- Add an IP address to a specific set:

`ipset add {{set_name}} {{192.168.1.25}}`

- Delete an ip from a set `test_set`:

`ipset del {{test_set}} {{192.168.1.25}}`

- Save an ip set (it depends on the distribution at which file you can save a set to be used from the ipset system service):

`ipset save {{test_set}} > /etc/ipset.conf`

# ipset

> A quick and easy tool to create IP sets for firewall rules

- Create an ip set named test_set which will contain ip addresses:

`ipset create test_set hash:ip`

- Destroy test_set:

`ipset x (or) destroy test_set`

- Add an ip to the previously created set:

`ipset add test_set 192.168.1.25`

- Delete an ip from a set:

`ipset del test_set 192.168.1.25`

- Save an ip set (it depends on the distibution at which file you can save a set to be used from the ipset system service):

`ipset save test_set > /etc/ipset.conf`


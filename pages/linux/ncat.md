# ncat

> `cat` over networks
> Use the normal cat functionality over networks

- Listen for input on the specified port and write it to the specified file:

`ncat -l {{port}} > /path/to/file`

- Write output of specified file to the specified host on the specified port:

`ncat {{address}} {{port}} < /path/to/file`

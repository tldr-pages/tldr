# ncat

> Read, write, redirect, and encrypt data across a network.
> An alternative implementation of a similar utility called `netcat`/`nc`.
> More information: <https://nmap.org/ncat/guide/index.html>.

- Listen for input on the specified port and write it to the specified file:

`ncat -l {{port}} > {{path/to/file}}`

- Accept multiple connections and keep ncat open after they have been closed:

`ncat -lk {{port}}`

- Write output of specified file to the specified host on the specified port:

`ncat {{address}} {{port}} < {{path/to/file}}`

- Accept multiple incoming connections on an encrypted channel evading detection of traffic content:

`ncat --ssl -k -l {{port}}`

- Connect to an open `ncat` connection over SSL:

`ncat --ssl {{host}} {{port}}`

- Check connectivity to a remote host on a particular port with timeout:

`ncat -w {{seconds}} -vz {{host}} {{port}}`

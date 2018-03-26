# ncat

> Use the normal `cat` functionality over networks.

- Listen for input on the specified port and write it to the specified file:

`ncat -l {{port}} > {{path/to/file}}`

- Accept multiple connections and keep ncat open after they have been closed:

`ncat -lk {{port}}`

- Write output of specified file to the specified host on the specified port:

`ncat {{address}} {{port}} < {{path/to/file}}`

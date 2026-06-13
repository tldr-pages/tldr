# rpcmap.py

> Lookup listening MSRPC interfaces using a string binding (e.g., `ncacn_ip_tcp:host[port]`).
> Part of the Impacket suite.
> More information: <https://github.com/fortra/impacket>.

- Connect to an MSRPC interface using a string binding (e.g., `ncacn_ip_tcp:host[port]`):

`rpcmap.py {{stringbinding}}`

- Bruteforce UUIDs even if the MGMT interface is available:

`rpcmap.py -brute-uuids {{stringbinding}}`

- Bruteforce operation numbers (opnums) for discovered UUIDs:

`rpcmap.py -brute-opnums {{stringbinding}}`

- Bruteforce major versions of found UUIDs:

`rpcmap.py -brute-versions {{stringbinding}}`

- Specify a target IP address manually:

`rpcmap.py -target-ip {{ip_address}} {{stringbinding}}`

- Authenticate to the RPC interface with username and password:

`rpcmap.py -auth-rpc {{domain}}/{{username}}:{{password}} {{stringbinding}}`

- Authenticate using NTLM hashes for RPC:

`rpcmap.py -hashes-rpc {{LMHASH:NTHASH}} {{stringbinding}}`

- Enable debug output for verbose information:

`rpcmap.py -debug {{stringbinding}}`

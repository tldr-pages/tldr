# sockstat

> List open Internet or UNIX domain sockets.
> More information: <https://man.freebsd.org/cgi/man.cgi?sockstat>.

- View which users/processes are [l]istening on which ports:

`sockstat -l`

- Show information for IPv[4]/IPv[6] sockets [l]istening on specific [p]orts using a specific [P]rotocol:

`sockstat -{{4|6}} -l -P {{tcp|udp|sctp|divert}} -p {{port1,port2...}}`

- Also show [c]onnected sockets, not resolving [n]umeric UIDs to user names and using a [w]ider field size:

`sockstat -cnw`

- Only show sockets that belong to a specific [j]ail ID or name in [v]erbose mode:

`sockstat -jv`

- Display the protocol [s]tate and the remote [U]DP encapsulation port number, if applicable (these are currently only implemented for SCTP and TCP):

`sockstat -sU`

- Display the [C]ongestion control module and the protocol [S]tack, if applicable (these are currently only implemented for TCP):

`sockstat -CS`

- Only show Internet sockets if the local and foreign addresses are not in the loopback network prefix 127.0.0.0/8, or do not contain the IPv6 loopback address ::1:

`sockstat -L`

- Do not show the header ([q]uiet mode), showing [u]nix sockets and displaying the `inp_gencnt`:

`sockstat -qui`

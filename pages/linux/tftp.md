# tftp

> Trivial File Transfer Protocol client.
> More information: <https://manned.org/tftp>.

- Connect to a TFTP server for an interactive mode, specifying its IP address and port:

`tftp {{server_ip}} {{port}}`

- Connect to a TFTP server and execute a TFTP [c]ommand:

`tftp {{server_ip}} -c {{command}}`

- Connect to a TFTP server using IPv6 and force originating port to be in [R]ange:

`tftp {{server_ip}} -6 -R {{port}}:{{port}}`

- [Interactive] Set the transfer mode to binary or ASCII through the tftp client:

`mode {{binary|ascii}}`

- [Interactive] Download file from a server through the tftp client:

`get {{file}}`

- [Interactive] Upload file to a server through the tftp client:

`put {{file}}`

- [Interactive] Exit the tftp client:

`quit`

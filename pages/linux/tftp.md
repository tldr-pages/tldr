# tftp

> Trivial File Transfer Protocol client.
> More information: <https://manned.org/tftp.1>.

- Connect to a TFTP server specifying its IP address and port:

`tftp {{server_ip}} {{port}}`

- Connect to a TFTP server and execute a TFTP [c]ommand:

`tftp {{server_ip}} -c {{command}}`

- Connect to a TFTP server using IPv6 and force originating port to be in [R]ange:

`tftp {{server_ip}} -6 -R {{port}}:{{port}}`

- Set the transfer mode to binary or ASCIi through the tftp client:

`mode {{binary|ascii}}`

- Download file from a server through the tftp client:

`get {{file}}`

- Upload file to a server through the tftp client:

`put {{file}}`

- Exit the tftp client:

`quit`

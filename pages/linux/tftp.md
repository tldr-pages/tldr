# tftp

> Trivial File Transfer Protocol client.
> More information: <https://manned.org/tftp.1>.

- Connect to a TFTP server specifying its IP address and port:

`tftp {{server_ip}} {{port}}`

- Connect to a TFTP server and execute a TFTP [c]ommand:

`tftp {{server_ip}} -c {{command}}`

- Connect to a TFTP server using IPv6 and force originating port to be in [R]ange:

`tftp {{server_ip}} -6 -R {{port}}:{{port}}`

- Set transfer mode to binary:

`mode binary`

- Download file:

`get {{file}}`

- Upload file:

`put {{file}}`

- Exit tftp:

`quit`

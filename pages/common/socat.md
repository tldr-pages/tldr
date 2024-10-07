# socat

> Multipurpose relay (SOcket CAT).
> More information: <http://www.dest-unreach.org/socat/>.

- Listen to a port, wait for an incoming connection and transfer data to STDIO:

`sudo socat - TCP-LISTEN:8080,fork`

- Listen on a port using SSL and print to STDOUT:

`sudo socat OPENSSL-LISTEN:4433,reuseaddr,cert=./cert.pem,cafile=./ca.cert.pem,key=./key.pem,verify=0 STDOUT`

- Create a connection to a host and port, transfer data in STDIO to connected host:

`sudo socat - TCP4:www.example.com:80`

- Forward incoming data of a local port to another host and port:

`sudo socat TCP-LISTEN:80,fork TCP4:www.example.com:80`

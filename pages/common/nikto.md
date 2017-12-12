#nikto

> Web server scanner which performs comprehensive tests against web servers for multiple 
> items, including over 6700 potentially dangerous files/programs.

- To update to the latest plugins and databases.

`perl nikto.pl -update`

- The most basic Nikto scan requires simply a host to target:

`perl nikto.pl -h 192.168.0.1`

- To check on a different port.

`perl nikto.pl -h 192.168.0.1 -p 443`

- Ports and protocols may also be specified by using a full URL syntax.

`perl nikto.pl -h https://192.168.0.1:443/`

- Scan multiple ports in the same scanning session.

`perl nikto.pl -h 192.168.0.1 -p 80,88,443`

- Set the proxy on the command line.

`perl nikto.pl -h localhost -useproxy http://localhost:8080/`


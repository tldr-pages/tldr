> Ping with Http protocol. 
> Measure the latency and throughput of a webserver.
> Homepage: <https://www.vanheusden.com/httping/>.

- Ping the webserver on host 'localhost':

`httping -g http://localhost/`

- Ping the webserver on host 'localhost' and portnumber '1000':

`httping -h localhost -p 1000`

- Ping the webserver on host 'localhost' using an SSL connection:

`httping -l -g https://localhost/`

- Ping the webserver on host 'localhost' using the Basic HTTP Authentication:

`httping -g http://localhost/ -U username -P password`

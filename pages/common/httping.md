# httping

> Measure the latency and throughput of a webserver.

- Ping the webserver on host 'localhost':

`httping -g http://localhost/`

- Ping the webserver on host 'localhost' and portnumber '1000':

`httping -h localhost -p 1000`

- Ping the webserver on host 'localhost' using an SSL connection:

`httping -l -g https://localhost/`

- Ping the web server on host 'localhost' using HTTP basic authentication:

`httping -g http://localhost/ -U username -P password`

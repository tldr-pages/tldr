# httping

> Measures the latency of a webserver.

- Measure latency of webserver using a URL:

`httping -g {{URL}}`

*Example:*

`httping -g google.com`

- Measure latency of a webserver using a hostname:

`httping -h {{hostname}}`

*Example:*

`http -h localhost`

- Measure latency using a specific port:

`httping {{webserver}} -p {{port}}`

- Measure latency a given number of times:

`httping -c {{count}} {{webserver}}`

- Measure latency using SSL (for this to work you need to give a 'https'-url or a 443 portnumber):

`httping -l {{webserver}}`

- Measure latency use basic authentication mechanism with a username and password:

`httping {{webserver}} -A -U {{username}} -P {{password}}`

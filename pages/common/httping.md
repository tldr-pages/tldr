# httping

> Measures the latency of a webserver.

- Measure latency of webserver using a URL:

`httping -g {{URL}}`

- Measure latency of webserver using a hostname:

`httping -h {{hostname}}`

- Measure latency using a specific port:

`httping {{webserver}} -p {{port}}`

- Measure latency only a specific number of times:

`httping -c {{count}} {{webserver}}`

- Measure latency using SSL (for this to work you need to give a 'https'-url or a 443 portnumber):

`httping -l {{webserver}}`

- Measure latency using authentication:

`httping {{webserver}} -A -U {{username}} -P {{password}}`

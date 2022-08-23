# jmeter

> Open source java application designed for load testing functional behavior and measure performance.
> More information: <https://jmeter.apache.org>.

- Run jmeter in cli mode for a test plan:

`jmeter -n -t {{name}}.jmx`
    
- Run jmeter and specify the log output:

`jmeter -n -t {{name}}.jmx -l {{logfile}}.jtl`

- Run jmeter using a proxy server and a port:

`jmeter -n -t {{name}}.jmx -H {{proxy_server_url}} -P {{port}}`

- Run jmeter with user defined variables:

`jmeter -J{{key}}={{value}} -n -t {{file_name}}.jmx`

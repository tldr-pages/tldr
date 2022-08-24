# jmeter

> Open source java application designed for load testing functional behavior and measure performance.
> More information: <https://jmeter.apache.org>.

- Run in nongui mode for a specific test plan:

`jmeter --nongui --testfile {{path/to/file}}.jmx`
- Use a specific log file:

`jmeter --nogui --testfile {{path/to/file}}.jmx --logfile {{path/to/logfile}}.jtl`

- Use a specific proxy server and a specific port:

`jmeter --nongui --testfile {{path/to/file}}.jmx --proxyHost {{127.0.0.1}} --proxyPort {{8888}}`

- Define user variables:

`jmeter --jmeterproperty {{key}}='{{value}}' --nongui --testfile {{path/to/file}}.jmx`

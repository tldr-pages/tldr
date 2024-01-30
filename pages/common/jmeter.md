# jmeter

> Open source Java application designed for load testing functional behavior and measure performance.
> More information: <https://jmeter.apache.org>.

- Run a specific test plan in nongui mode:

`jmeter --nongui --testfile {{path/to/file}}.jmx`

- Run a test plan in nongui mode using a specific log file:

`jmeter --nogui --testfile {{path/to/file}}.jmx --logfile {{path/to/logfile}}.jtl`

- Run a test plan in nongui mode using a specific proxy:

`jmeter --nongui --testfile {{path/to/file}}.jmx --proxyHost {{127.0.0.1}} --proxyPort {{8888}}`

- Run a test plan in nongui mode using a specific JMeter property:

`jmeter --jmeterproperty {{key}}='{{value}}' --nongui --testfile {{path/to/file}}.jmx`

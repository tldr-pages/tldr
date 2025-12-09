# jmeter

> Open source Java application designed for load testing functional behavior and measure performance.
> More information: <https://jmeter.apache.org/usermanual/get-started.html#options>.

- Run a specific test plan in nongui mode:

`jmeter {{[-n|--nongui]}} {{[-t|--testfile]}} {{path/to/file.jmx}}`

- Run a test plan in nongui mode using a specific log file:

`jmeter {{[-n|--nongui]}} {{[-t|--testfile]}} {{path/to/file.jmx}} {{[-l|--logfile]}} {{path/to/logfile.jtl}}`

- Run a test plan in nongui mode using a specific proxy:

`jmeter {{[-n|--nongui]}} {{[-t|--testfile]}} {{path/to/file.jmx}} {{[-H-|--proxyHost]}} {{127.0.0.1}} {{[-P|--proxyPort]}} {{8888}}`

- Run a test plan in nongui mode using a specific JMeter property:

`jmeter {{[-n|--nongui]}} {{[-t|--testfile]}} {{path/to/file.jmx}} {{[-J|--jmeterproperty]}} {{key}}='{{value}}'`

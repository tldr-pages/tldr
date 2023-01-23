# jmeter

> Nyílt forráskódú java alkalmazás, amelyet a funkcionális viselkedés terheléses tesztelésére és a teljesítmény mérésére terveztek. További információ: <https://jmeter.apache.org>.

- Egy adott tesztterv futtatása nongui üzemmódban:

`jmeter --nongui --testfile {{path/to/file}}.jmx`

- Egy tesztterv futtatása nongui módban egy adott naplófájl segítségével:

`jmeter --nogui --testfile {{path/to/file}}.jmx --logfile {{path/to/logfile}}.jtl`

- Egy tesztterv futtatása nongui módban egy adott proxy használatával:

`jmeter --nongui --testfile {{path/to/file}}.jmx --proxyHost {{127.0.0.1}} --proxyPort {{8888}}`

- Tesztterv futtatása nongui módban egy adott JMeter-tulajdonság használatával:

`jmeter --jmeterproperty {{key}}='{{value}}' --nongui --testfile {{path/to/file}}.jmx`

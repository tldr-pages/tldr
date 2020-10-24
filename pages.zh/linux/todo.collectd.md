# collectd

> System statistics collection daemon.
> More information: <https://collectd.org/>.

- Show usage help, including the program version:

`collectd -h`

- Test the configuration file and then exit:

`collectd -t`

- Test plugin data collection functionality and then exit:

`collectd -T`

- Start collectd:

`collectd`

- Specify a custom configuration file location:

`collectd -C {{path/to/file}}`

- Specify a custom PID file location:

`collectd -P {{path/to/file}}`

- Don't fork into the background:

`collectd -f`

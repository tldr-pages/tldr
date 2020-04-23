# ioping

> Monitor I/O latency in real time.
> More information: <https://github.com/koct9i/ioping>.

- Show disk I/O latency using the default values and the current directory:

`ioping .`

- Measure latency on /tmp using 10 requests of 1 megabyte each:

`ioping -c 10 -s 1M /tmp`

- Measure disk seek rate on /dev/sda:

`ioping -R /dev/sda`

- Measure disk sequential speed on /dev/sda:

`ioping -RL /dev/sda`

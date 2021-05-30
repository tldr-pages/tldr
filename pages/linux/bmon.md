# bmon

> Monitor bandwidth and capture network related statistics.
> More information: <https://github.com/tgraf/bmon>.

- Display the list of all the interfaces:

`bmon -a`

- Display data transfer rates in bits per second:

`bmon -b`

- Set policy to define which network interface(s) is/are displayed:

`bmon -p {{interface_1,interface_2,interface_3}}`

- Set interval (in seconds) in which rate per counter is calculated:

`bmon -R {{2.0}}`

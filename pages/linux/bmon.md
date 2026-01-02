# bmon

> Monitor bandwidth and capture network related statistics.
> More information: <https://manned.org/bmon>.

- Display the list of all the interfaces:

`bmon {{[-a|--show-all]}}`

- Display data transfer rates in bits per second:

`bmon {{[-b|--use-bit]}}`

- Specify the policy to define which network interface(s) is/are displayed:

`bmon {{[-p|--policy]}} {{interface_1,interface_2,interface_3,...}}`

- Specify the interval (in seconds) in which rate per counter is calculated:

`bmon {{[-R|--rate-interval]}} {{2.0}}`

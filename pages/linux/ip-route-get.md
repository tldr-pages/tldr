# ip route get

> Get a single route to a destination and print its contents exactly as the kernel sees it.
> More information: <https://manned.org/ip-route>.

- Print route to a destination (1.1.1.1):

`ip route get 1.1.1.1`

- Print route to a destination (1.1.1.1) from source (0.0.0.0):

`ip route get 1.1.1.1 from 0.0.0.0`

- Print route from 127.0.0.2 to 127.0.0.1:

`ip route get 127.0.0.1 from 127.0.0.2`

- Print route from 127.0.0.1 to 0.0.0.0:

`ip route get 0.0.0.0 from 127.0.0.1`

- Print route from 0.0.0.0 to 127.0.0.1:

`ip route get 127.0.0.1 from 0.0.0.0`

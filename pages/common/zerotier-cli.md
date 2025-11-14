# zerotier-cli

> Control the local ZeroTier virtual network service.
> More information: <https://github.com/zerotier/ZeroTierOne/blob/dev/doc/zerotier-cli.1.md>.

- Join a network:

`sudo zerotier-cli join {{network_id}}`

- List networks:

`sudo zerotier-cli listnetworks`

- List peers in a readable format:

`sudo zerotier-cli peers`

- Leave a network:

`sudo zerotier-cli leave {{network_id}}`

- Display the status of ZeroTier One:

`sudo zerotier-cli {{[info|status]}}`

# zerotier-cli

> Manage a local ZeroTier node and its network memberships.
> Most of these commands require `sudo`.
> More information: <https://docs.zerotier.com/cli/>.

- Show node status:

`zerotier-cli status`

- List networks this node knows about:

`zerotier-cli listnetworks`

- Join a network:

`zerotier-cli join {{network_id}}`

- Leave a network:

`zerotier-cli leave {{network_id}}`

- Show peers:

`zerotier-cli listpeers`

- Output JSON:

`zerotier-cli -j {{command}}`

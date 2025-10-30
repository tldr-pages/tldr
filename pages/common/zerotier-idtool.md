# zerotier-idtool

> Manage ZeroTier identities (public/private keys, addresses).
> More information: <https://man.archlinux.org/man/zerotier-idtool.1.en>.

- Generate a new identity pair and write to two files:

`zerotier-idtool generate {{identity.public}} {{identity.secret}}`

- Show the ZeroTier address for an identity file:

`zerotier-idtool get {{identity.public}}`

- Initialize a moon definition and write JSON to a file:

`zerotier-idtool initmoon {{identity.public}} > {{moon.json}}`

# zerotier-idtool

> Create and manipulate ZeroTier identities.
> See also: `zerotier-cli`, `zerotier-one`.
> More information: <https://github.com/zerotier/ZeroTierOne/blob/dev/doc/zerotier-idtool.1.md>.

- Generate a new ZeroTier identity and output the secret part to `stdout`:

`zerotier-idtool generate`

- Generate a new ZeroTier identity and save the secret and public parts to files:

`zerotier-idtool generate {{path/to/identity.secret}} {{path/to/identity.public}}`

- Generate a new ZeroTier identity with a specific hexadecimal vanity prefix (can take a long time):

`zerotier-idtool generate {{path/to/identity.secret}} {{path/to/identity.public}} {{vanity_prefix}}`

- Extract the public portion from a secret identity:

`zerotier-idtool getpublic {{path/to/identity.secret}}`

- Sign a file using a secret identity:

`zerotier-idtool sign {{path/to/identity.secret}} {{path/to/file}}`

- Verify a signed file using a public identity and a hexadecimal signature:

`zerotier-idtool verify {{path/to/identity.public}} {{path/to/file}} {{signature_hex}}`

- Locally validate an identity's key and proof of work:

`zerotier-idtool validate {{path/to/identity.public}}`

- Display help:

`zerotier-idtool help`

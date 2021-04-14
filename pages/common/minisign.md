# minisign

> A simple and secure utility to sign and verify files. Compatible with `signify`.
> More information: <https://jedisct1.github.io/minisign/>.

- Generate a new keypair at the default location:

`minisign -G`

- Sign a file:

`minisign -Sm {{file}}

- Sign a file adding a trusted (signed) and an untrusted (unsigned) comment in the signature:

`minisign -Sm {{file}} -c {{"This comment is untrusted."}} -t {{"This comment is trusted."}}

- Verify a file and the trusted comments in its signature using the specified public key file:

`minisign -Vm {{file}} -p {{publickey.pub}}`

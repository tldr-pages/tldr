# pip hash

> Compute hashes of package archives for verification.
> More information: <https://pip.pypa.io/en/stable/cli/pip_hash/>.

- Generate hash for a package file:

`pip hash {{path/to/package.whl}}`

- Generate hash using a specific algorithm:

`pip hash {{[-a|--algorithm]}} {{sha256|sha384|sha512|...}} {{path/to/package.whl}}`

- Generate hashes for multiple files:

`pip hash {{path/to/package1.whl path/to/package2.whl ...}}`

- Generate hash for downloaded archive:

`pip hash {{path/to/package.tar.gz}}`

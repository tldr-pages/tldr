# systemd-id128

> Generate and print sd-128 identifiers.
> More information: <https://www.freedesktop.org/software/systemd/man/systemd-id128.html>.

- Generate a new random identifier:

`systemd-id128 new`

- Print the identifier of the current machine:

`systemd-id128 machine-id`

- Print the identifier of the current boot:

`systemd-id128 boot-id`

- Print the identifier of the current service invocation (this is available in systemd services):

`systemd-id128 invocation-id`

- Generate a new random identifier and print it as an UUID (five groups of digits separated by hyphens):

`systemd-id128 new --uuid`

# iw reg

> Manage WLAN regulatory domains.
> More information: <https://wireless.docs.kernel.org/en/latest/en/users/documentation/iw.html>.

- Display the current regulatory domain:

`iw reg get`

- Set the regulatory domain according to ISO 3166-1 alpha-2:

`sudo iw reg set {{US|JP|FI|...}}`

- Reload the kernel's regulatory database:

`sudo iw reg reload`

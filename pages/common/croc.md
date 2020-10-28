# croc

> Send and receive files easily and securely over any network.
> More information: <https://github.com/schollz/croc>.

- Send a file or folder:

`croc send {{path/to/file}}`

- Send a file or folder with a specific passphrase:

`croc send --code {{passphrase}} {{path/to/file}}`

- Receive a file or folder on receiving machine:

`croc {{passphrase}}`

- Send and connect over a custom relay:

`croc --relay {{ip_to_relay}} send {{path/to/file}}`

- Receive and connect over a custom relay:

`croc --relay {{ip_to_relay}} {{passphrase}}`

- Host a croc relay on the default ports:

`croc relay`

- Display parameters and options for a croc command:

`croc {{send|relay}} --help`

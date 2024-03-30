# systemd-creds

> List, show, encrypt and decrypt service credentials.
> More information: <https://www.freedesktop.org/software/systemd/man/systemd-creds.html>.

- Encrypt a file and set a specific name:

`systemd-creds encrypt --name={{name}} {{path/to/input_file}} {{path/to/output}}`

- Decrypt the file again:

`systemd-creds decrypt {{path/to/input_file}} {{path/to/output_file}}`

- Encrypt text from `stdin`:

`echo -n {{text}} | systemd-creds encrypt --name={{name}} - {{path/to/output}}`

- Encrypt the text and append it to the service file (the credentials will be available in `$CREDENTIALS_DIRECTORY`):

`echo -n {{text}} | systemd-creds encrypt --name={{name}} --pretty - - >> {{service}}`

- Create a credential that is only valid until the given timestamp:

`systemd-creds encrypt --not-after="{{timestamp}}" {{path/to/input_file}} {{path/to/output_file}}`

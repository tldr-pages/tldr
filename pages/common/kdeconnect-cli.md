# kdeconnect-cli

> KDE Connect CLI.
> More information: <https://kdeconnect.kde.org>.

- List all devices:

`kdeconnect-cli --list-devices`

- List all reachable devices:

`kdeconnect-cli --list-available`

- Request pairing with a specific device, specifying its ID:

`kdeconnect-cli --pair --device {{device_id}}`

- Request pairing with a specific device, specifying its name:
- Ring a device, specifying its name:

`kdeconnect-cli --pair --name {{device_name}}`
`kdeconnect-cli --ring --name {{device_name}}`

- Share a file or URL to a paired device, specifying its ID: 

`kdeconnect-cli --share {{path/to/file|URL}} --device {{device_id}}`

- Send an SMS with an optional attachment to a specific number:

`kdeconnect-cli --name {{device_name}} --send-sms {{message}} --destination {{phone_number}} --attachment {{path/to/file}}`

- Unlock a specific device:

`kdeconnect-cli --name {{device_name}} --unlock`

- Simulate a key press on a specific device:

`kdeconnect-cli --name {{device_name}} --send-keys {{key}}`

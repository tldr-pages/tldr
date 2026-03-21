# wacli

> WhatsApp command-line client for sending messages, managing chats, and contacts.
> Some subcommands such as `send`, `messages`, `chats`, and `contacts` have their own usage documentation.
> More information: <https://github.com/steipete/wacli>.

- Authenticate via QR code:

`wacli auth`

- Synchronize messages once and exit:

`wacli sync --once`

- Send a text message to a phone number:

`wacli send text --to {{phone_number}} --message "{{message}}"`

- List messages from a specific chat:

`wacli messages list --chat {{phone_number}}@s.whatsapp.net --json`

- List all chats:

`wacli chats list --json`

- Search contacts by name:

`wacli contacts search "{{name}}" --json`

- Run diagnostics on the store:

`wacli doctor`

- Display version:

`wacli version`

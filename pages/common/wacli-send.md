# wacli send

> Send messages and status via WhatsApp.
> Some subcommands such as `file` and `text` have their own usage documentation.
> More information: <https://wacli.sh/send.html>.

- Send a text message to a phone number or a chatroom's JID:

`wacli send text --to {{phone_number|jid}} --message "{{message}}"`

- Send a file, sticker, or voice note to a phone number or a chatroom's JID:

`wacli send {{file|sticker|voice}} --to {{phone_number|jid}} --file {{path/to/file}}`

- Send a location coordinate with a name to a phone number or a chatroom's JID:

`wacli send location --to {{phone_number|jid}} --latitude {{latitude}} --longitude {{longitude}} --name "{{place_name}}"`

- Send a new poll to a phone number or a chatroom's JID:

`wacli send poll --to {{phone_number|jid}} --question "{{question}}" --option "{{option1}}" --option "{{option2}}" ...`

- Create a new status from an image or video file, with an optional caption:

`wacli send status --file {{path/to/file}} --message "{{caption}}"`

- Create a new text status with a specific background color and font size:

`wacli send status --message "{{Hello World!}}" --background-color "{{#008888}}" --font {{1}}`

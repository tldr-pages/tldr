# wacli send text

> Send a text message via WhatsApp.
> See also: `wacli send file`.

- Send a text message to a phone number:

`wacli send text --to {{phone_number}} --message "{{message}}"`

- Send a text message to a specific JID:

`wacli send text --to {{phone_number}}@s.whatsapp.net --message "{{message}}"`

- Send a text message with a custom timeout:

`wacli send text --to {{phone_number}} --message "{{message}}" --timeout {{10m}}`

- Send a text message using a custom store path:

`wacli send text --to {{phone_number}} --message "{{message}}" --store {{path/to/store}}`

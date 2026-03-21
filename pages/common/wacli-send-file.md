# wacli send file

> Send a file (image, video, audio, or document) via WhatsApp.
> See also: `wacli send text`.

- Send a file to a phone number:

`wacli send file --to {{phone_number}} --file {{path/to/file}}`

- Send a file to a specific JID:

`wacli send file --to {{phone_number}}@s.whatsapp.net --file {{path/to/file}}`

- Send a file with a custom timeout:

`wacli send file --to {{phone_number}} --file {{path/to/file}} --timeout {{10m}}`

# openclaw message

> Send messages through OpenClaw channels.
> More information: <https://github.com/openclaw/openclaw>.

- Send a message to a phone number (WhatsApp):

`openclaw message send {{[-t|--target]}} {{+1234567890}} {{[-m|--message]}} "{{Hello}}"`

- Send a message to a specific channel:

`openclaw message send --channel {{telegram}} {{[-t|--target]}} {{user_id}} {{[-m|--message]}} "{{Hello}}"`

- View help:

`openclaw message {{[-h|--help]}}`

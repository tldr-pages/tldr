# bun feedback

> Sends feedback to `Bun`.
> More information: <https://bun.com/docs/feedback#use-bun-feedback>.

- Send text as feedback:

`bun feedback "{{Feedback text!}}"`

- Send file as feedback:

`bun feedback {{path/to/file}}`

- Send feedback with email address attached:

`bun feedback {{path/to/file|text}} {{[-e|--email]}} {{email@address}}`

# bun feedback

> Sends feedback to `Bun`.
> More information: <https://bun.com/docs/feedback#use-bun-feedback>.

- Send text as feedback:

`bun feedback "{{Feedback text!}}"`

- Send one or more files as feedback:

`bun feedback {{path/to/file1 path/to/file2 ...}}`

- Send feedback with email address attached:

`bun feedback {{path/to/file|text}} {{[-e|--email]}} {{email@address}}`

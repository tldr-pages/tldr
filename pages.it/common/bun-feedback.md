# bun feedback

> Invia feedback a Bun.
> Maggiori informazioni: <https://bun.com/docs/feedback#use-bun-feedback>.

- Invia del testo come feedback:

`bun feedback "{{Testo Feedback!}}"`

- Invia uno o più file come feedback:

`bun feedback {{percorso/al/file1 percorso/al/file2 ...}}`

- Invia feedback con un indirizzo email allegato:

`bun feedback {{path/to/file|text}} {{[-e|--email]}} {{email@indirizzo}}`

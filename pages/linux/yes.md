# yes

> Output a string repeatedly until stopped.
> More information: <https://man7.org/linux/man-pages/man1/yes.1.html>.

- Repeatedly output “y”:
  `yes`

- Repeatedly output a custom string:
  `yes {{hello}}`

- Use yes to automatically confirm prompts (for example, when removing files):
  `yes | rm {{*.txt}}`

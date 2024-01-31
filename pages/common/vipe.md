# vipe

> Run a text editor in the middle of a UNIX pipeline.
> More information: <https://joeyh.name/code/moreutils/>.

- Edit the output of `command1` before piping it into `command2`:

`{{command1}} | vipe | {{command2}}`

- Buffer the output of `command1` in a temporary file with the specified file extension in order to aid syntax highlighting:

`{{command1}} | vipe --suffix {{json}} | {{command2}}`

- Use the specified text editor:

`{{command1}} | EDITOR={{vim}} vipe | {{command2}}`

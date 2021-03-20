# nms

> Command line tool that recreates the famous data decryption effect seen in the 1992 movie Sneakers from stdin.
> More information: <https://github.com/bartobri/no-more-secrets>.

- Decrypt text after a keystroke:

`echo "{{Hello, World!}}" | nms`

- Decrypt the output of `ls -la` automatically:

`{{ls -la}} | nms -a`

- Decrypt the content of a file automatically with a custom output color:

`cat {{path/to/file}} | nms -a -f {{blue|white|yellow|black|magenta|green|red}}`

- Clear the screen before decrypting:

`{{command}} | nms -a -c`

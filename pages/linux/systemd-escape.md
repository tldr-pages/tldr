# systemd-escape

> Escape strings for usage in systemd unit names.
> More information: <https://www.freedesktop.org/software/systemd/man/systemd-escape.html>.

- Escape the given text:

`systemd-escape {{text}}`

- Reverse the escaping process:

`systemd-escape --unescape {{text}}`

- Treat the given text as a path:

`systemd-escape --path {{text}}`

- Append the given suffix to the escaped text:

`systemd-escape --suffix {{suffix}} {{text}}`

- Use a template and inject the escaped text:

`systemd-escape --template {{template}} {{text}}`

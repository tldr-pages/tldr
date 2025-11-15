# airpaste

> Share messages and files on the same network using mDNS.
> More information: <https://github.com/mafintosh/airpaste>.

- Wait for a message and display it when received:

`airpaste`

- Send text:

`echo {{text}} | airpaste`

- Send a file:

`airpaste < {{path/to/file}}`

- Receive a file:

`airpaste > {{path/to/file}}`

- Create or join a channel:

`airpaste {{channel_name}}`

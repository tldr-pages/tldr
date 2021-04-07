# sic

> Simple IRC client.
> Part of the suckless tools.
> More information: <https://tools.suckless.org/sic/>.

- Connect to a host with the specified nickname:

`sic -h {{irc.ofct.net}} -n {{$USER}}`

- Connect to a given host, using a given nickname and password:

`sic -h {{host}} -n {{nickname}} -k {{password}}`

- Join a channel:

`:j #{{channel}}<Enter>`

- Send a message to a channel or user:

`:m #{{channel|user}}<Enter>`

- Set default channel or user:

`:s #{{channel|user}}<Enter>`

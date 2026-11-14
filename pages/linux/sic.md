# sic

> Simple IRC client.
> Part of the suckless tools.
> More information: <https://manned.org/sic>.

- Connect to the default host (irc.ofct.net) with the nickname set in the `$USER` environment variable:

`sic`

- Connect to a given host, using a given nickname:

`sic -h {{host}} -n {{nickname}}`

- Connect to a given host, using a given nickname and password:

`sic -h {{host}} -n {{nickname}} -k {{password}}`

- [Interactive] Join a channel:

`:j #{{channel}}`

- [Interactive] Send a message to a channel or user:

`:m #{{channel|user}}`

- [Interactive] Set default channel or user:

`:s #{{channel|user}}`

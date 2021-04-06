# sic

> simple irc client.
> Part of the suckless.org tools.
> More information: <https://tools.suckless.org/sic/>.

- Connect to a host with the specified nickname:

`sic -h {{irc.ofct.net}} -n {{$USER}}`

- Connect to a different host with PASS connection password:

`sic -h {{host}} -n {{nickname}} -k {{password}}`

- Usage with highlighted alerts on mention of your username:

`sic | awk '/username/ {printf "\a"}1'`

- Join a channel (stdin):

`:j #{{channel}}`

- Send a message (stdin):

`:m #{{channel}}/{{user}}`

- Set default channel or user (stdin):

`:s #{{channel}}/{{user}}`

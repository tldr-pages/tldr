# sic

> simple irc client.
> Part of suckless.org tools.
> More information: <https://tools.suckless.org/sic/>.

- Connect to host (default: irc.oftc.net) with nickname (default: $USER):

`sic -n {{nickname}}`

- Connect to a different host with PASS connection password:

`sic -n {{nickname}} -p {{password}}`

- Usage with highlighted alerts on mention of your username:

`sic | awk '/username/ {printf "\a"}1'`

- Join a channel (stdin):

`:j #{{channel}}`

- Send a message (stdin):

`:m #{{channel}}/{{user}}`

- Set default channel or user (stdin):

`:s #{{channel}}/{{user}}`

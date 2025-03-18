# logread

> Read the `logd` ring buffer log.
> More information: <https://openwrt.org/docs/guide-user/base-system/log.essentials>.

- Print the log:

`logread`

- Print a specified number of messages:

`logread -l {{N}}`

- Filter messages by (Keyword/Regular Expression):

`logread -e {{pattern}}`

- Print log messages as they happen:

`logread -f`

- Display help:

`logread -h`

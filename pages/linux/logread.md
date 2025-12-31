# logread

> Read the `logd` ring buffer log.
> More information: <https://openwrt.org/docs/guide-user/base-system/log.essentials>.

- Print the log:

`logread`

- Print `n` messages:

`logread -l {{n}}`

- Filter messages by (Keyword/`regex`):

`logread -e {{pattern}}`

- Print log messages as they happen:

`logread -f`

- Display help:

`logread -h`

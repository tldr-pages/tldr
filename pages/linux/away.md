# away

> Locks terminal with an away message.
> More information: <https://manned.org/away>.

- Lock terminal and set away message:

`away {{message}}`

- Lock terminal and enable mail check:

`away {{[-c|--mail]}} {{message}}`

- Lock terminal and disable mail check:

`away {{[-C|--nomail]}} {{message}}`

- Lock terminal and sleep background tasks for number of seconds:

`away {{[-t|--time]}} {{seconds}} {{message}}`

- Lock terminal and check mail if at least one inbox hasn't received new mail:

`away {{[-p|--persist]}} {{message}}`

- Lock terminal and check mail until at least one inbox has received new mail:

`away {{[-P|--nopersist]}} {{message}}`

- Display help:

`away {{[-h|--help]}}`

- Display version:

`away {{[-v|--version]}}`

# makoctl dismiss

> Dismiss notifications in mako.
> More information: <https://manned.org/makoctl>.

- Dismiss the most recent notification:

`makoctl dismiss`

- Dismiss a specific notification by ID:

`makoctl dismiss -n {{notification_id}}`

- Dismiss all notifications:

`makoctl dismiss {{[-a|--all]}}`

- Dismiss all notifications in the same group:

`makoctl dismiss --group`

- Dismiss without adding to history:

`makoctl dismiss --no-history`

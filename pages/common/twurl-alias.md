# twurl alias

> Manage aliases for API endpoint paths.
> More information: <https://github.com/twitter/twurl>.

- List all aliases:

`twurl alias`

- Create an alias for an endpoint path:

`twurl alias {{alias_name}} {{/1.1/statuses/home_timeline.json}}`

- Create an alias for posting tweets:

`twurl alias {{tweet}} {{/1.1/statuses/update.json}}`

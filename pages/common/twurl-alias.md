# twurl alias

> Manage aliases for the Twitter API command-line client `twurl`.
> More information: <https://github.com/twitter/twurl>.

- List all aliases:

`twurl alias`

- Create an alias for a Twitter API endpoint:

`twurl alias {{alias_name}} {{endpoint}}`

- Create an alias for the home timeline endpoint:

`twurl alias {{home}} {{/1.1/statuses/home_timeline.json}}`

- Use an alias:

`twurl {{alias_name}}`

- Remove an alias:

`twurl alias rm {{alias_name}}`
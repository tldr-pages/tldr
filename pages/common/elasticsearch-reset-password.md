# elasticsearch-reset-password

> Reset the passwords of users in the native realm and built-in users.
> More information: <https://www.elastic.co/docs/reference/elasticsearch/command-line-tools/reset-password>.

- Reset the password of the user to an auto-generated value and print it in the console:

`elasticsearch-reset-password {{[-u|--username]}} {{user}}`

- Prompt interactively to reset the password for a native user:

`elasticsearch-reset-password {{[-u|--username]}} {{user}} {{[-i|--interactive]}}`

- Interactively reset the password for a user at a specified Elasticsearch node URL:

`elasticsearch-reset-password --url {{host}}:{{port}} {{[-u|--username]}} {{user}} {{[-i|--interactive]}}`

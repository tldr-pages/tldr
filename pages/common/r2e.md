# r2e

> Forward RSS feeds to an email address.
> Requires a configured `sendmail` or SMTP setup.
> More information: <https://manned.org/r2e>.

- Create a new feed database that sends email to an email address:

`r2e new {{email_address}}`

- Subscribe to a feed:

`r2e add {{feed_name}} {{feed_uri}}`

- Send new stories to an email address:

`r2e run`

- List all feeds:

`r2e list`

- Delete a feed at a specified index:

`r2e delete {{index}}`

- Display help:

`r2e {{[-h|--help]}}`

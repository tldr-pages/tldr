# r2e

> Forwards RSS feeds to an email address.
> Requires a configured `sendmail` or smtp setup.
> More information: <https://github.com/rss2email/rss2email>.

- Create a new feed database that sends email to an email address:

`r2e new {{email_address}}`

- Subscribe to a feed:

`r2e add {{feed_name}} {{feed_URI}}`

- Send new stories to an email address:

`r2e run`

- List all feeds:

`r2e list`

- Delete a feed at a specified index:

`r2e delete {{index}}`

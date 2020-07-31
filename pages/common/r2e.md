# r2e

> Forwards RSS feeds to your email address. More information: https://github.com/rss2email/rss2email.

> Requires a configured sendmail or smtp setup

- Create a new feed database that sends email to your email address.

`r2e new {{email_address}}`

- Subscribe to a feed.

`r2e add {{feed_name}} {{feed_URI}}`

- Send new stories to your email.

`r2e run`

- List all feeds.

`r2e list`

- Delete a feed at index.

`r2e delete {{index}}`

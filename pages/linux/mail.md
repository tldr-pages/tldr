# mail

> Send and receive email from the command line

- Send an email with a subject line

`mail -s "Hello, world" user@example.org < /dev/null`

- Send an email to multiple recipients

`mail -s "Hello, world" user@example.org,user@example.com < /dev/null`

- Send a file attachment

`mail -a /path/to/file -s "Here is your file" user@example.org < /dev/null`

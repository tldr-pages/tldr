# swaks

> Swiss Army Knife SMTP, the all-purpose SMTP transaction tester.
> More information: <https://github.com/jetmore/swaks/blob/develop/doc/base.pod>.

- Deliver a standard test email to `user@example.com` on port 25 of `test-server.example.net`:

`swaks --to {{user@example.com}} --server {{test-server.example.net}}`

- Deliver a standard test email, requiring CRAM-MD5 authentication as user `me@example.com`. An "X-Test" header will be added to the email body:

`swaks --to {{user@example.com}} --from {{me@example.com}} --auth {{CRAM-MD5}} --auth-user {{me@example.com}} --header-X-Test "{{test_email}}"`

- Test a virus scanner using EICAR in an attachment. Don't show the message DATA part:

`swaks -t {{user@example.com}} --attach - --server {{test-server.example.com}} --suppress-data {{path/to/eicar.txt}}`

- Test a spam scanner using GTUBE in the body of an email, routed via the MX records for `example.com`:

`swaks --to {{user@example.com}} --body {{path/to/gtube_file}}`

- Deliver a standard test email to `user@example.com` using the LMTP protocol via a UNIX domain socket file:

`swaks --to {{user@example.com}} --socket {{/var/lda.sock}} --protocol {{LMTP}}`

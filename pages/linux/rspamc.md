# rspamc

> Command line client for rspamd servers.

- Train the bayesian filter to recognise an email as spam:

`rspamc learn_spam {{path/to/email_file}}`

- Train the bayesian filter to recognise an email as ham:

`rspamc learn_ham {{path/to/email_file}}`

- Generate a manual report on an email:

`rspamc symbols {{path/to/email_file}}`

- Show server statistics:

`rspamc stat`

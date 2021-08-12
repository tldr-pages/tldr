# rspamc

> Client de linie de comandă pentru serverele rspamd.

- Instruiți filtrul bayesian pentru a recunoaște un e-mail ca spam:

`rspamc learn_spam {{path/to/email_file}}`

- Instruiți filtrul bayesian pentru a recunoaște un e-mail ca șuncă:

`rspamc learn_ham {{path/to/email_file}}`

- Generează un raport manual pe un e-mail:

`rspamc symbols {{path/to/email_file}}`

- Arată statisticile serverului:

`rspamc stat`

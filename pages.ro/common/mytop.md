# mytop

> Afișează informații despre performanța serverului MySQL, cum ar fi `top'.
> Mai multe informaţii: <http://jeremy.zawodny.com/mysql/mytop/mytop.html>

- Porniţi partea mea:

`mytop`

- Conectați-vă cu un nume de utilizator și o parolă specificate:

`mytop -u {{user}} -p {{password}}`

- Conectați-vă cu un nume de utilizator specificat (utilizatorului i se va solicita o parolă):

`mytop -u {{user}} --prompt`

- Nu arătaţi fire inactive (de dormit):

`mytop -u {{user}} -p {{password}} --noidle`

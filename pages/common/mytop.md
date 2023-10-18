# mytop

> Display MySQL server performance info like `top`.
> More information: <http://jeremy.zawodny.com/mysql/mytop/mytop.html>.

- Start `mytop`:

`mytop`

- Connect with a specified username and password:

`mytop -u {{user}} -p {{password}}`

- Connect with a specified username (the user will be prompted for a password):

`mytop -u {{user}} --prompt`

- Do not show any idle (sleeping) threads:

`mytop -u {{user}} -p {{password}} --noidle`

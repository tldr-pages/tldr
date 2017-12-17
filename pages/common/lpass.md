# lpass

> Command line interface for LastPass Password Manager

- Login to your LastPass account, by entering your Master Password when promted:

`lpass login {{username}}`

- Show login status:

`lpass status`

- List all sites grouped by category:

`lpass ls`

- Show password for a specified entry (usually the website url):

`lpass show {{identifier}} --password`

- Generate a new password and add to LastPass:

`lpass generate --username {{username}} --url {{url}} {{identifier}} {{password_lenght}}`

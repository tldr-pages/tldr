# lpass

> Command line interface for LastPass Password Manager.

- Login to your LastPass account, by entering your Master Password when prompted:

`lpass login {{username}}`

- Show login status:

`lpass status`

- List all sites grouped by category:

`lpass ls`

- Generate a new password and add to LastPass:

`lpass generate --username {{username}} --url {{gmail.com}} {{gmail.com}} {{password_length}}`

- Show password for a specified entry (usually the website url):

`lpass show {{gmail.com}} --password`

# usermod

> Modifies a user account.

- Change a user's name:

`usermod -l {{newname}} {{user}}`

- Add user to supplementary groups (mind the whitespace):

`usermod -a -G {{group1,group2}} {{user}}`

- Create a new home directory for a user and move their files to it:

`usermod -m -d {{path/to/home}} {{user}}`

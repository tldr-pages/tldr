# usermod

> Modifies a user account.
> More information: <https://manned.org/usermod>.

- Change a user's name:

`usermod --login {{newname}} {{user}}`

- Add user to supplementary groups (mind the whitespace):

`usermod --append --groups {{group1,group2}} {{user}}`

- Create a new home directory for a user and move their files to it:

`usermod --move-home --home {{path/to/home}} {{user}}`

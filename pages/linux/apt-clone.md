# apt-clone

> Clone/backup/restore the package state of a Debian-based system.
> More information: <https://github.com/mvo5/apt-clone>.

- Clone the package state of the current system into a specified directory:

`apt-clone clone {{path/to/directory}}`

- Create a clone file (`tar.gz`) for backup purposes:

`apt-clone clone --destination {{path/to/backup.tar.gz}}`

- Restore the package state from a clone file:

`apt-clone restore {{path/to/backup.tar.gz}}`

- Show information about a clone file (e.g., the release, architecture):

`apt-clone info {{path/to/backup.tar.gz}}`

- Check if the clone file can be restored on the current system:

`apt-clone restore {{path/to/backup.tar.gz}} --destination {{path/to/restore}}`

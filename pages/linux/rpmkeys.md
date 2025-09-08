# rpmkeys

> Tool to import and remove RPM keys for RPM repositories.
> When adding an RPM repository, you must also import the corresponding RPM key.
> More information: <https://rpm-software-management.github.io/rpm/man/rpmkeys.8>.

- List all imported RPM keys. Also outputs its Key ID needed for deleting a imported RPM key:

`sudo rpmkeys --list`

- Remove/Delete a previously imported RPM key, given by its 16-Number/Letters Key ID:

`sudo rpmkeys --delete {{5a278d9c-5bbc73cb}}`

- Import an RPM key of repository:

`sudo rpmkeys --import {{path/to/rpm_key}}`

# rpmkeys

> Tool to import and remove rpm keys of for rpm repositories.
> When adding a rpm respository then you also must import the corresponding rpm key.
> More information: <https://rpm-software-management.github.io/rpm/man/rpmkeys.8>.

- List all imported rmp keys. Also outputs its Key ID needed for deleting a imported rpm key:

`sudo rpmkeys --list`

- Remove/Delete a previously imported rpm key, given by its 16-Number/Letters Key ID:

`sudo rpmkeys --delete {{5a278d9c-5bbc73cb}}`

- Import a rpm key of repository:

`sudo rpmkeys --import {{path_to_rpm_key_to_import}}`

# ci

> Check in RCS revisions (store file changes in the Revision Control System).
> See also: `co`, `rcs`, `rcsdiff`, `rlog`.
> More information: <https://manned.org/ci>.

- Check in a file and keep the working file unlocked:

`ci -u {{path/to/file}}`

- Check in a file and keep the working file locked:

`ci -l {{path/to/file}}`

- Check in a file with a specific log message:

`ci -m "{{log_message}}" {{path/to/file}}`

- Check in a file, unlocking it but leaving the working file read-only:

`ci {{path/to/file}}`

- Force check-in even if there are no changes:

`ci -f -u {{path/to/file}}`

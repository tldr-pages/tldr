# rcs

> Revision Control System - manage RCS file attributes.
> See also: `ci`, `co`, `rcsdiff`, `rlog`.
> More information: <https://manned.org/rcs>.

- Unlock a revision locked by another user (requires access):

`rcs -u {{path/to/file}}`

- Lock a specific revision of a file:

`rcs -l{{revision}} {{path/to/file}}`

- Set the strict locking mode (require lock for check-in):

`rcs -L {{path/to/file}}`

- Add or replace a log message for a specific revision:

`rcs -m{{revision}}:"{{new_message}}" {{path/to/file}}`

- Delete a specific revision from the RCS file:

`rcs -o{{revision}} {{path/to/file}}`

# chcat

> Change SELinux security category for files.
> Categories provide an additional level of access control based on MCS (Multi-Category Security).
> See also: `chcon`, `semanage`.
> More information: <https://manned.org/chcat>.

- List all available categories:

`sudo chcat {{[-L|--list]}}`

- Add a category to a file:

`sudo chcat +{{CategoryName}} {{path/to/file}}`

- Remove a category from a file:

`sudo chcat -- -{{CategoryName}} {{path/to/file}}`

- Set specific categories for a file (replacing existing ones):

`sudo chcat {{CategoryName1,CategoryName2,...}} {{path/to/file}}`

- Display the categories of a file:

`ls {{[-Z|--context]}} {{path/to/file}}`

- Remove all categories from a file:

`sudo chcat {{[-d|--delete]}} {{path/to/file}}`

# finger

> User information lookup program.

- Display information about currently logged in users:

`finger`

- Display information about a specific user:

`finger {{username}}`

- Display the user's login name, real name, terminal name and write status (as a "\*" after the terminal name if write permission is denied), idle time, login time, office location and office phone number:

`finger -s`

- Produce multi-line format displaying same information as `-s` as well as user's home directory, home phone number, login shell, mail status as well as contents of files ".plan", ".project", ".pgpkey", and ".foward" in their home directory:

`finger -l`

- Prevent matching against user's names and only use login names:

`finger -m`

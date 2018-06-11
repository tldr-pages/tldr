# finger

> User information lookup program.

- Display the user's login name, real name, terminal name and write status (as a "\*" after the terminal name if write permission is denied), idle time, login time, office location and office phone number:

`finger -s`

- Produce a multi-line format displaying all the information described for the option ```-s``` as well as the user's home directory, home phone number, login shell, mail status, and the contents of the files ".plan", ".project", ".pgpkey" and ".forward" from the user's home directory:

`finger -l`

- Prevent the ```-l``` option of finger from displaying the contents of the ".plan", ".project" and ".pgpkey" files:

`finger -m`

- Display another user's information:

`finger {{username}}`

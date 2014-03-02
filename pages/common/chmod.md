# chmod

> Change the permission of a file or directory

- Give the user rights to execute a file/directory

`chmod u+x {{file}}`

- Give the user rights to read and write to a file/directory

`chmod u+wr {{file}}`

- Removes executable rights from group

`chmod g-x {{file}}`

- Gives the user, group and owner rights to execute and read

`chmod ugo+xr {{file}}`

- Formula for chmod

`chmod {{who}} {{operation}} {{perm}} {{file}}`

*{{who}} is any combination of `u` (user), `g` (group), `o` (owner)
*{{operation}} is either `+` or `-`
*{{perm}} is any combination of `r` (read), `w` (write), `x` (execute)

- Changing permissions alternate form

*{executable} = 1
*{write} = 2
*{read} = 4
*{read + executable} = 5
*{rwx} = 7

- Example: `chmod 755 {{file}}`
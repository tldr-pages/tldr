# umask

> Set permission for newly created files for current user.

- Display mask value as octal:

`umask`

- Set the mask using octal notation:

`umask {{nnnn}}`

- Display mask value in human-readable mode:

`umask -S`

- Set the mask using symbolic notation:

`umask {{ u - user | g - groups | o - others | a - all }}{{ + enable | - disable | = enable specified }}{{ r - read | w -write | x- execute }}`

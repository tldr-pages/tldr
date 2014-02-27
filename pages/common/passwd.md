#passwd

> passwd is a tool on most Unix and Unix-like operating systems used to change a user's password.

* Change your password. ( You may need to use **sudo** ). The {{options}} flag can use -a, -d, -e, -h, -S, -i, -k, -l, -m , -q, -r, -u, -v, -x  as arguments.

`passwd {{options}} {{new password}}`


* Gives the current statuts of the user. The status information consists of 7 fields, sutch as the password status, the username, the date, the age etc...   

`passwd -S`

* Make the password of the account blank ( It will set the named account passwordless. )

`passwd -d`

* Change the password of the specified user.

`passwd {{username}} {{new password}}`

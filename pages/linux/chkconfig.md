# chkconfig

> Manage service boot runlevel.

- List services with runlevel:

`chkconfig --list`

- List one service with runlevel:

`chkconfig --list ntpd`

- Enable service at boot:

`chkconfig sshd on`

- Enable service at boot at runlevel

`chkconfig --level 3 sshd on`

- Disable service at boot:

`chkconfig ntpd off`

- Disable service at boot at runlevel

`chkconfig --level 3 ntpd off`

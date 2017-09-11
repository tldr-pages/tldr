# init

> Its primary role is to create processes from a script stored in the file /etc/inittab.

- Shutsdown the system:

`init 0`

- Single user mode or emergency mode:

`init 1`

- Reboot the system:

`init 6`

- Boot directly into a single user shell:

`init -b`

- Tell the init command to enter the maintenance mode:

`init s`

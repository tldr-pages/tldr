# debugfs

> An interactive ext2/ext3/ext4 filesystem debugger.

- Open the filesystem in read only mode:

`debugfs {{/dev/sdXN}}`

- Open the filesystem in read write mode:

`debugfs -w {{/dev/sdXN}}`

- Read commands from cmd_file file, execute them and exit:

`debugfs -f {{path/to/cmd_file}}`

- View the filesystem stats in debugfs console:

`debugfs: stats`

- Close the filesystem:

`debugfs: close -a`

- List all available commands:

`debugfs: lr`

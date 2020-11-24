# chmod


> chmod or change mode allows users to change permissions for a file
> more information: https://linux.die.net/man/1/chmod


- `chmod {{xxx}}`
- Changes the permission of a file. 1 for execute only, 2 for write only, and 4 for read only. 
- Each digit represents a permission for owner,group, and others in order.

```sh
chmod 400 # Owner can read, group and others have no permissions
chmod 700 # Owner can read/write/execute, group and others have no permissions 
chmod 777 # Owner,Group, and Others can read/write/execute. NEVER DO THIS
```

- Suppresses errors
> chmod -f

- Changes permissions recursively 
> chmod -r

- To see any other possible options:
> chmod --help

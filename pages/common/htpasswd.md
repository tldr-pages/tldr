# htpasswd

> Create and manage htpasswd files to protect web server directories using basic authentication.

- Create/overwrite htpasswd file:

`htpasswd -c {{file_path}} {{user_name}}`

- Add user to htpasswd file or update existing user:

`htpasswd {{file_path}} {{user_name}}`

- Add user to htpasswd file without password verification (for script usage):

`htpasswd -b {{file_path}} {{user_name}} {{password}}`

- Delete user from htpasswd file:

`htpasswd -D {{file_path}} {{user_name}}`

- Verify user password:

`htpasswd -v {{file_path}} {{user_name}}`

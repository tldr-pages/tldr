# pwpolicy

> Get and set password policies.
> More information: <https://keith.github.io/xcode-man-pages/pwpolicy.8.html>.

- Change password for specified user:

`sudo pwpolicy -a {{authenticator}} -u {{username}} -setpassword "{{new_password}}"`

- Disable a user account:

`sudo pwpolicy -u {{username}} -disableuser`

- Enable a user account:

`sudo pwpolicy -u {{username}} -enableuser`

- Get list of password hashes stored on disk for a user account:

`sudo pwpolicy -u {{username}} -gethashtypes`

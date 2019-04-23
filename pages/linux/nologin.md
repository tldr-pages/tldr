# nologin

> Alternative shell that prevents a user's login.

- Set user's login shell to `nologin` to prevent user logging-in:

`chsh -s {{user}} nologin`

- Customize message for users with the login shell of `nologin`:

`echo "{{declined_login_message}}" > /etc/nologin.txt`

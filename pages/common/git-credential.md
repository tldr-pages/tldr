# git credential

> Retrieve and store user credentials.
> More information: <https://git-scm.com/docs/git-credential>.

- Display credential information, retrieving the username/password from config files:

`echo {{"url=http://example.com"}} | git credential fill`

- Send credential information to configured credential helpers to store for later use:

`echo {{"url=http://example.com"}} | git credential approve`

- Send credential information to configured credential helpers to erase:

`echo {{"url=http://example.com"}} | git credential reject`

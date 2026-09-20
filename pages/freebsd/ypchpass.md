# ypchpass

> Add or change NIS user database information, including login shell and password.
> See also: `chpass`.
> More information: <https://man.freebsd.org/cgi/man.cgi?query=ypchpass>.

- Add or change NIS user database information for the current user interactively:

`ypchpass`

- Specify the [h]ostname or address of an NIS server to query:

`su -c 'ypchpass -h {{hostname}} {{username}}'`

- Specify a particular NIS [d]omain (system domain name by default):

`su -c 'ypchpass -d {{domain}} {{username}}'`

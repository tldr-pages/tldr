# gyb

> Command line tool for locally backing up Gmail messages using Gmail's API over HTTPS.
> More information: <https://github.com/GAM-team/got-your-back>.

- Estimate the number and the size of all emails on your Gmail account:

`gyb --email {{email@gmail.com}} --action estimate`

- Backup your Gmail account to a specific directory:

`gyb --email {{youremail@gmail.com}} --action backup --local-folder {{path/to/directory}}`

- Backup only important or starred emails from your Gmail account to the default local folder:

`gyb --email {{youremail@gmail.com}} --search "is:important OR is:starred"`

- Restore from a local folder to your Gmail account:

`gyb --email {{youremail@gmail.com}} --action restore --local-folder {{path/to/directory}}`

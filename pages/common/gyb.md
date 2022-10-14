# Got Your Back - GYB

> Command line tool for backing up your Gmail messages to your computer using Gmail's API over HTTPS.
> More information: <https://github.com/GAM-team/got-your-back>.

- Estimate the number and the size of all mails on youremail@gmail.com:

`gyb --email {{youremail@gmail.com}} --action estimate`

- Backup from youremail@gmail.com to your {{path/to/directory}}:

`gyb --email {{youremail@gmail.com}} --action backup --local-folder {{path/to/directory}}`

- Backup only important or starred emails from {{youremail@gmail.com}} to the default local folder GYB-GMail-Backup-youremail@gmail.com:

`gyb --email {{youremail@gmail.com}} --search "is:important OR is:starred"`

- Restore from your local-folder to {{youremail@gmail.com}}:

`gyb --email {{youremail@gmail.com}} --action restore --local-folder {{path/to/directory}}`

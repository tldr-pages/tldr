# fwconsole

> Manage and configure your FreePBX system (PBX server).
> More information: <https://sangomakb.atlassian.net/wiki/spaces/PG/pages/41779247/fwconsole+commands+13>.

- Reload FreePBX configurations:

`fwconsole reload`

- Start Asterisk and other commands needed by FreePBX:

`fwconsole start`

- Stop Asterisk and other commands needed by FreePBX:

`fwconsole stop`

- View and update settings:

`fwconsole setting {{keyword}} {{new_value}}`

- List available backups:

`fwconsole backup --list`

- List available FreePBX commands:

`fwconsole list`

- Change ownership of all files and directories that FreePBX needs to be owned by the apache user:

`fwconsole chown`

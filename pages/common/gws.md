# gws

> Google Workspace CLI for Drive, Gmail, Calendar, Sheets, Docs, Chat, Admin, and more.
> More information: <https://github.com/googleworkspace/cli>.

- Set up Google Cloud project configuration and authenticate:

`gws auth setup`

- Log in with OAuth scopes for specific services:

`gws auth login {{[-s|--scopes]}} {{drive,gmail,sheets}}`

- Display help for a service, including generated methods and helper commands:

`gws {{service}} --help`

- List Google Drive files with a limited page size:

`gws drive files list --params '{{{"pageSize": 10}}}'`

- Create a Google Sheets spreadsheet:

`gws sheets spreadsheets create --json '{{{"properties": {"title": "Q1 Budget"}}}}'`

# gws

> Google Workspace CLI for Drive, Gmail, Calendar, Sheets, Docs, Chat, and more.
> Commands are generated dynamically from Google's Discovery Service.
> More information: <https://github.com/googleworkspace/cli>.

- Walk through Google Cloud project and OAuth setup:

`gws auth setup`

- Log in with OAuth:

`gws auth login`

- List Drive files:

`gws drive files list --params '{"pageSize": 10}'`

- Create a Google Sheet:

`gws sheets spreadsheets create --json '{"properties": {"title": "Q1 Budget"}}'`

- Preview a Chat API request without sending it:

`gws chat spaces messages create --params '{"parent": "spaces/xyz"}' --json '{"text": "Deploy complete."}' --dry-run`

- Show help for a dynamically discovered method:

`gws drive files list --help`

- Print the installed CLI version:

`gws --version`

# gws

> Google Workspace CLI for services such as Drive, Gmail, Calendar, Sheets, Docs, Chat, and Admin.
> More information: <https://github.com/googleworkspace/cli>.

- Set up authentication:

`gws auth setup`

- Log in to Google Workspace:

`gws auth login`

- List files in Google Drive with a page size limit:

`gws drive files list --params '{"pageSize": 10}'`

- Send an email:

`gws gmail +send --to {{user@example.com}} --subject "{{subject}}" --body "{{message_body}}"`

- Show today's calendar agenda:

`gws calendar +agenda`

- Upload a file to Google Drive:

`gws drive +upload {{path/to/file}} --name "{{file_name}}"`

- Export credentials for use in CI or headless environments:

`gws auth export --unmasked > {{path/to/credentials.json}}`

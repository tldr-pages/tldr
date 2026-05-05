# razify

> CLI tool to scan, validate, audit and document `.env` files.
> Detects leaked secrets, validates missing variables, and gives a health score.
> More information: <https://github.com/Hossiy21/razify>.

- Scan a `.env` file for leaked secrets:

`razify scan {{path/to/.env}}`

- Validate missing variables against a template:

`razify validate {{path/to/.env}} {{path/to/.env.example}}`

- Install a pre-commit hook to block secret commits:

`razify guard install`

- Audit a `.env` file and get a health score out of 100:

`razify audit {{path/to/.env}} {{path/to/.env.example}}`

- Auto-generate documentation from `.env.example`:

`razify docs {{path/to/.env.example}}`

- Compare two environment files:

`razify diff {{path/to/.env}} {{path/to/.env.staging}}`

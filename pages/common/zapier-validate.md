# zapier validate

> Validate a Zapier integration.
> More information: <https://github.com/zapier/zapier-platform/blob/main/packages/cli/docs/cli.md#validate>.

- Validate an integration:

`zapier validate`

- Validate an integration without style checks:

`zapier validate --without-style`

- Validate an integration without running the build script:

`zapier validate --skip-build`

- Validate an integration with additional debug output:

`zapier validate {{[-d|--debug]}}`

- Validate an integration with a different output structure:

`zapier validate {{[-f|--format]}} {{plain|json|raw|row|table}}`

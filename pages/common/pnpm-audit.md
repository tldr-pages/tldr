# pnpm audit

> Scan project dependencies.
> Check for known security issues with the installed packages.
> More information: <https://pnpm.io/cli/audit>.

- Identify vulnerabilities in the project:

`pnpm audit`

- Automatically fix vulnerabilities:

`pnpm audit fix`

- Generate a security report in JSON format:

`pnpm audit --json > {{path/to/audit-report.json}}`

- Audit only [D]ev dependencies:

`pnpm audit --dev`

- Audit only [P]roduction dependencies:

`pnpm audit --prod`

- Exclude optional dependencies from the audit:

`pnpm audit --no-optional`

- Ignore registry errors during the audit process:

`pnpm audit --ignore-registry-errors`

- Filter advisories by severity (low, moderate, high, critical):

`pnpm audit --audit-level {{severity}}`

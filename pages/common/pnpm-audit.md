# pnpm audit

> Scans project dependencies.
> Checks for known security issues with the installed packages.
> More information: <https://pnpm.io/cli/audit>.

- Identify vulnerabilities in the project:

`pnpm audit`

- Automatically fix vulnerabilities:

`pnpm audit fix`

- Generate a security report in JSON format:

`pnpm audit --json > audit-report.json`

- Only audit dev dependencies:

`pnpm audit --dev`

- Only audit production dependencies:

`pnpm audit --prod`

- Don't audit optionalDependencies:

`pnpm audit --no-optional`

- Ignore registry errors during the audit process:

`pnpm audit --ignore-registry-errors`

# npm audit

> Scan for known vulnerabilities in project dependencies.
> Reports vulnerabilities and suggests remediation.
> More information: <https://docs.npmjs.com/cli/npm-audit>.

- Scan project’s dependencies for known vulnerabilities:

`npm audit`

- Automatically fix vulnerabilities:

`npm audit fix`

- Update the lock file without modifying the `node_modules` directory:

`npm audit fix --package-lock-only`

- Perform a dry run. Simulate the fix process without making any changes:

`npm audit fix --dry-run`

- Output audit results in JSON format:

`npm audit --json`

- Configure the audit to only fail on vulnerabilities above a specified severity:

`npm audit --audit-level={{info|low|moderate|high|critical}}`

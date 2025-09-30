# npm audit

> Scan for known vulnerabilities in project dependencies.
> Reports vulnerabilities and suggests remediation.
> More information: <https://docs.npmjs.com/cli/npm-audit>.

- Scan the project's dependencies for known vulnerabilities:

`npm audit`

- Automatically fix vulnerabilities in the project's dependencies:

`npm audit fix`

- Force an automatic fix to dependencies with vulnerabilities:

`npm audit fix {{[-f|--force]}}`

- Update the lock file without modifying the `node_modules` directory:

`npm audit fix --package-lock-only`

- Perform a dry run. Simulate the fix process without making any changes:

`npm audit fix --dry-run`

- Output audit results in JSON format:

`npm audit --json`

- Configure the audit to only fail on vulnerabilities above a specified severity:

`npm audit --audit-level {{info|low|moderate|high|critical}}`

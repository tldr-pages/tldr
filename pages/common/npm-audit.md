# npm audit

> Scan for known vulnerabilities in project dependencies.
> Reports vulnerabilities and suggests remediation.
> More information: <https://docs.npmjs.com/cli/npm-audit>.

- Check your project for vulnerabilities-  Scans your project’s dependencies for known vulnerabilities:

`npm audit`

- Automatically fix vulnerabilities-  Attempts to fix vulnerabilities by updating to safe package versions:

`npm audit fix`

- Update only the `package-lock.json`-  Updates the lock file without modifying the `node_modules` directory:

`npm audit fix --package-lock-only`

- Perform a dry run-  Simulates the fix process without making any changes:

`npm audit fix --dry-run`

- Output audit results in JSON format-  Provides audit results in a structured JSON format for processing:

`npm audit --json`

- Set a minimum severity level- Configures the audit to only fail on vulnerabilities above a specified severity:

`npm audit --audit-level={{info|low|moderate|high|critical}}`

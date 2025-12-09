# bun-audit

> Check installed packages for known security vulnerabilities.
> More information: <https://bun.com/docs/pm/cli/audit>.

- Audit all dependencies in a project with a `bun.lock` file:

`bun audit`

- Show only vulnerabilities at or above a specific severity level:

`bun audit --audit-level {{low|moderate|high|critical}}`

- Audit only production dependencies:

`bun audit --prod`

- Ignore a specific CVE ID:

`bun audit --ignore {{CVE-XXXX-YYYY}}`

- Output the raw JSON report:

`bun audit --json`

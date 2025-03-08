# composer audit

> Analyze a PHP project's dependencies to detect known security vulnerabilities and list affected packages.
> See also: `composer`.
> More information: <https://getcomposer.org/doc/03-cli.md#audit>.

- Check for security vulnerabilities in your current project:

`composer audit`

- Omit dev dependencies in the audit:

`composer audit --no-dev`

- Filter vulnerabilities by output format:

`composer audit --format {{table|plain|json|summary}}`

- Output audit results to a file in JSON format:

`composer audit --format json > audit_report.json`

- Verify whether a specific package in your project is affected by security issues:

`composer audit {{vendor}}/{{package}}`

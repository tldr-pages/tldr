# bagel

> Scan a development environment for exposed secrets, insecure settings, and credential files.
> Only metadata and locations are reported, never secret values.
> More information: <https://github.com/boostsecurityio/bagel#usage>.

- Scan the local system and print the report as JSON:

`bagel scan`

- Scan the local system and display the report as a table:

`bagel scan {{[-f|--format]}} table`

- Scan specific directories and save the report to a file:

`bagel scan --base-dirs {{path/to/directory1,path/to/directory2,...}} {{[-o|--output]}} {{path/to/report.json}}`

- Scan and exit with code 2 if any findings are detected (useful in scripts):

`bagel scan --strict`

- Preview which credentials would be redacted from AI CLI session logs and shell history:

`bagel scrub --dry-run`

- Redact credentials from AI CLI session logs and shell history without asking for confirmation:

`bagel scrub {{[-y|--yes]}}`

- Redact credentials from a specific file:

`bagel scrub --file {{path/to/file}}`

- Display version:

`bagel version`

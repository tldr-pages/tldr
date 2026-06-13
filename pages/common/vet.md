# vet

> Scan package manifests, directories, container images, or GitHub repositories to identify vulnerabilities, malicious packages, and enforce security policies using CEL expressions.
> More information: <https://safedep.github.io/vet/vet.html>.

- Scan the current directory:

`vet scan {{[-D|--directory]}} .`

- Scan the `package-lock.json` manifest file:

`vet scan {{[-M|--manifests]}} {{path/to/manifest_file}}`

- Scan with filter to fail on any critical vulnerability found in the codebase:

`vet scan {{[-D|--directory]}} {{path/to/directory}} --filter 'vulns.critical.exists(p, true)' --filter-fail`

- Scan any OSS package for malware:

`vet inspect malware --purl {{package_url}}`

- Start the MCP server for AI enabled security in code editors like Cursor:

`vet server mcp`

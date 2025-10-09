# vet

> Scan package manifests, directories, container images, or GitHub repositories to identify vulnerabilities, malicious packages, and enforce security policies using CEL expressions.
> More information: <https://safedep.github.io/vet>.

- Scan the current directory:

`vet scan -D .`

- Scan the `package-lock.json` manifest file:

`vet scan -M package-lock.json`

- Scan with filter to fail on any critical vulnerability found in the codebase:

`vet scan -D . --filter 'vulns.critical.exists(p, true)' --filter-fail`

- Scan any OSS package for malware:

`vet inspect malware --purl pkg:/npm/nyc-config@10.0.0`

- Manage and query cloud resources (control plane):

`vet cloud`

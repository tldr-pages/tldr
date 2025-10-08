# vet

> Scan package manifests, directories, container images, or GitHub repositories to identify vulnerabilities, malicious packages, and enforce security policies using CEL expressions.
> More information: <https://github.com/safedep/vet>

- Establish trust in open source software supply chain

`vet scan -D .`

- Scans the current directory.

`vet scan -M package-lock.json`

- Scans the `package-lock.json` manifest file

`vet scan -D . --filter 'vulns.critical.exists(p, true)' --filter-fail`

- Scan with filter to fail on any critical vulnerability found in the codebase.

`vet inspect malware --purl  pkg:/npm/nyc-config@10.0.0`

- Scan any OSS package for malware

`vet cloud`

- Manage and query cloud resources (control plane)

# grype

> Vulnerability scanner for container images and filesystems.
> More information: <https://github.com/anchore/grype>.

- Scan a container image:

`grype {{image:tag}}`

- Scan an image and display results in a specific format:

`grype {{image:tag}} {{[-o|--output]}} {{json|table|cyclonedx|cylonedx-json|sarif|template}}`

- Scan an image, ignoring unfixed vulnerabilities:

`grype {{image:tag}} --only-fixed`

- Scan an image and fail on vulnerabilities with a severity at or above the given level:

`grype {{image:tag}} {{[-f|--fail-on]}} {{negligible|low|medium|high|critical}}`

- Scan a local directory and save the report to a file:

`grype {{path/to/directory}} {{--file}} {{path/to/report}}`

- Update the vulnerability database:

`grype db update`

- Display the current database status:

`grype db status`

- Display help:

`grype {{[-h|--help]}}`

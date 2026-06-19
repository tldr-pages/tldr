# syft

> Generate a Software Bill of Materials (SBOM) from container images and filesystems.
> More information: <https://oss.anchore.com/docs/reference/syft/cli/>.

- Generate an SBOM from a container image:

`syft {{image:tag}}`

- Generate an SBOM from a local directory:

`syft {{path/to/directory}}`

- Generate an SBOM from a container archive file:

`syft {{path/to/archive.tar}}`

- Generate an SBOM in SPDX JSON format:

`syft {{image:tag}} {{[-o|--output]}} spdx-json`

- Generate an SBOM in CycloneDX JSON format:

`syft {{image:tag}} {{[-o|--output]}} cyclonedx-json`

- Write the SBOM to a file in a specific format:

`syft {{image:tag}} {{[-o|--output]}} {{format}}={{path/to/output_file}}`

- Display help:

`syft {{[-h|--help]}}`

- Display version:

`syft --version`

# gh attestation

> Download and verify artifact attestations to ensure their integrity and provenance.
> More information: <https://cli.github.com/manual/gh_attestation>.

- Download attestations for a local file associated with a specific repository:

`gh {{[at|attestation]}} download {{path/to/artifact.bin}} {{[-R|--repo]}} {{owner}}/{{repo}}`

- Download attestations for an OCI container image associated with an organization:

`gh {{[at|attestation]}} download oci://{{image_uri}} {{[-o|--owner]}} {{organization_name}}`

- Verify a local artifact online against attestations from a specific repository:

`gh {{[at|attestation]}} verify {{path/to/artifact.bin}} {{[-R|--repo]}} {{owner}}/{{repo}}`

- Verify an artifact, requiring it was signed by a specific reusable workflow for enhanced security:

`gh {{[at|attestation]}} verify {{path/to/artifact.bin}} {{[-o|--owner]}} {{organization_name}} --signer-workflow {{owner}}/{{repo}}/{{path/to/workflow.yml}}`

- Verify an artifact and output the detailed verification results as JSON for use in policy engines:

`gh {{[at|attestation]}} verify {{path/to/artifact.bin}} {{[-o|--owner]}} {{organization_name}} --format json`

- Perform a fully offline verification using a downloaded bundle and a custom trusted root file:

`gh {{[at|attestation]}} verify {{path/to/artifact.bin}} {{[-b|--bundle]}} {{path/to/bundle.jsonl}} --custom-trusted-root {{path/to/trusted_root.jsonl}}`

- Save the trusted root of signing certificates to a file for offline verification:

`gh {{[at|attestation]}} trusted-root > {{path/to/trusted_root.jsonl}}`

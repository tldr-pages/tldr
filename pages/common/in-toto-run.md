# in-toto-run

> Generating link metadata while carrying out a supply chain step.
> More information: <https://in-toto.readthedocs.io/en/latest/command-line-tools/in-toto-run.html>.

- Tag a Git repo and signing the resulting link file:

`in-toto-run {{[-n|--step-name]}} {{tag}} {{[-p|--products]}} {{.}} -k {{key_file}} -- {{git tag v1.0}}`

- Create a tarball, storing files as materials and the tarball as product:

`in-toto-run {{[-n|--step-name]}} {{package}} {{[-m|--materials]}} {{project}} {{[-p|--products]}} {{project.tar.gz}} -- {{tar czf project.tar.gz project}}`

- Generate signed attestations for review work:

`in-toto-run {{[-n|--step-name]}} {{review}} -k {{key_file}} {{[-m|--materials]}} {{document.pdf}} {{[-x|--no-command]}}`

- Scan the image using Trivy and generate link file:

`in-toto-run {{[-n|--step-name]}} {{scan}} -k {{key_file}} {{[-p|--products]}} {{report.json}} -- {{/bin/sh -c "trivy --output report.json --format json <IMAGE>"}}`

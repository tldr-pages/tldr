# gh attestation

> Download en verifieer artefactverklaringen om hun integriteit en herkomst te controleren.
> Meer informatie: <https://cli.github.com/manual/gh_attestation>.

- Download verklaringen voor een lokaal bestand dat aan een specifieke repository is gekoppeld:

`gh {{[at|attestation]}} download {{pad/naar/artefact.bin}} {{[-R|--repo]}} {{eigenaar}}/{{repository}}`

- Download verklaringen voor een OCI-containerimage die aan een organisatie is gekoppeld:

`gh {{[at|attestation]}} download oci://{{image_uri}} {{[-o|--owner]}} {{organisatienaam}}`

- Verifieer een lokaal artefact online aan de hand van verklaringen van een specifieke repository:

`gh {{[at|attestation]}} verify {{pad/naar/artefact.bin}} {{[-R|--repo]}} {{eigenaar}}/{{repository}}`

- Verifieer een artefact en vereis dat het is ondertekend door een specifieke herbruikbare workflow voor verbeterde beveiliging:

`gh {{[at|attestation]}} verify {{pad/naar/artefact.bin}} {{[-o|--owner]}} {{organisatienaam}} --signer-workflow {{eigenaar}}/{{repository}}/{{pad/naar/workflow.yml}}`

- Verifieer een artefact en toon de gedetailleerde verificatieresultaten als JSON voor gebruik in beleids-engines:

`gh {{[at|attestation]}} verify {{pad/naar/artefact.bin}} {{[-o|--owner]}} {{organisatienaam}} --format json`

- Voer een volledig offline verificatie uit met een gedownload bundle en een aangepast vertrouwd root-bestand:

`gh {{[at|attestation]}} verify {{pad/naar/artefact.bin}} {{[-b|--bundle]}} {{pad/naar/bundle.jsonl}} --custom-trusted-root {{pad/naar/vertrouwde_root.jsonl}}`

- Sla de vertrouwde root van ondertekeningscertificaten op in een bestand voor offline verificatie:

`gh {{[at|attestation]}} trusted-root > {{pad/naar/vertrouwde_root.jsonl}}`

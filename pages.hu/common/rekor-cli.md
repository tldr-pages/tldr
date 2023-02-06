# rekor-cli

> A szoftverprojektek ellátási láncában keletkező metaadatok megváltoztathatatlan, hamisításálló főkönyve. További információ: <https://github.com/sigstore/rekor>.

- Lelet feltöltése a Rekorba:

`rekor-cli upload --artifact {{path/to/file.ext}} --signature {{path/to/file.ext.sig}} --pki-format={{x509}} --public-key={{path/to/key.pub}}`

- Információk lekérése az átláthatósági napló bejegyzéseiről:

`rekor-cli get --uuid={{0e81b4d9299e2609e45b5c453a4c0e7820ac74e02c4935a8b830d104632fd2d1}}`

- Keresés a Rekor indexében a bejegyzések keresése az artefaktum alapján:

`rekor-cli search --artifact {{path/to/file.ext}}`

- Keresés a Rekor-indexben a bejegyzések keresése egy adott hash alapján:

`rekor-cli search --sha {{6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b}}`

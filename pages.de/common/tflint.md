# tflint

> Ein erweiterbarer Terraform-Linter zum Finden von Fehlern, Warnen vor veralteter Syntax und Durchsetzen von Best Practices.
> Weitere Informationen: <https://github.com/terraform-linters/tflint>.

- Plugin-Konfiguration initialisieren und deklarierte Plugins installieren:

`tflint --init`

- Die Terraform-Konfiguration im aktuellen Verzeichnis linten:

`tflint`

- Mit einer bestimmten Konfigurationsdatei linten:

`tflint --config {{pfad/zu/.tflint.hcl}}`

- Rekursiv in jedem Unterverzeichnis ausführen:

`tflint --recursive`

- Nur eine bestimmte Regel aktivieren, alle anderen Standards deaktivieren:

`tflint --only {{regelname}}`

- Eine bestimmte Regel deaktivieren:

`tflint --disable-rule {{regelname}}`

- Probleme automatisch beheben, wo möglich:

`tflint --fix`

- Ergebnisse im JSON-Format ausgeben (nützlich für CI/CD):

`tflint --format json`

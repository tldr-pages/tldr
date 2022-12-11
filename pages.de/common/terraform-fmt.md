# terraform fmt

> Formatierung der Konfiguration gemäß den Konventionen der Terraform-Sprache.
> Weitere Informationen: <https://www.terraform.io/docs/commands/fmt.html>.

- Formatieren der Konfiguration im aktuellen Verzeichnis:

`terraform fmt`

- Formatieren der Konfiguration im aktuellen Verzeichnis und den Unterverzeichnissen:

`terraform fmt -recursive`

- Anzeige der Unterschiede bei Formatierungsänderungen:

`terraform fmt -diff`

- Die Dateien mit Formatierungsinkonsistenzen werden nicht auf stdout ausgegeben:

`terraform fmt -list=false`

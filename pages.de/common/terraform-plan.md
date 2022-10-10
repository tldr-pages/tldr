# terraform plan

> Erzeugen und Anzeigen von Terraform-Ausführungsplänen.
> Weitere Informationen: <https://www.terraform.io/docs/cli/commands/plan.html>.

- Erzeugen und Anzeigen des Ausführungsplans im aktuellen Verzeichnis:

`terraform plan`

- Einen Plan zur Zerstörung aller derzeit existierenden entfernten Objekte anzeigen:

`terraform plan -destroy`

- Anzeigen eines Plans zur Aktualisierung des Terraform-Status und der Ausgabewerte:

`terraform plan -refresh-only`

- Werte für Eingabevariablen festlegen:

`terraform plan -var '{{name1}}={{wert1}}' -var '{{name2}}={{wert2}}'`

- Anzeigen eines Plans auf eine Teilmenge von Ressourcen:

`terraform plan -target {{resource_type.resource_name[index]}}`

- Ausgabe eines Plans als JSON:

`terraform plan -json`

- Ausgabe eines Plans in eine separate Datei:

`terraform plan -no-color > {{pfad/zu/datei}}`

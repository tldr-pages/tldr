# aws s3

> CLI für AWS S3. AWS S3 stellt Speicherplatz in der Cloud zur Verfügung.
> Weitere Informationen: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/index.html>.

- Liste alle Objekte in einem Bucket auf:

`aws s3 ls {{bucket_name}}`

- Synchronisiere Dateien und Verzeichnissen zu einem Bucket:

`aws s3 sync {{pfad/zu/datei_oder_verzeichnis}} s3://{{bucket_name}}`

- Synchronisiere Dateien und Verzeichnissen von einem Bucket:

`aws s3 sync s3://{{bucket_name}} {{pfad/zu/ziel}}`

- Synchronisiere Dateien und Verzeichnissen mit Ausnahmen:

`aws s3 sync {{pfad/zu/datei_oder_verzeichnis}} s3://{{bucket_name}} --exclude {{pfad/zu/datei}} --exclude {{pfad/zu/verzeichnis}}/*`

- Entferne ein Objekt von einem Bucket:

`aws s3 rm s3://{{bucket}}/{{pfad/zu/datei}}`

- Probelauf eines angegebenen Kommandos ohne dieses auszuführen:

`aws s3 {{befehl}} --dryrun`

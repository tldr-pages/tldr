# aws s3

> Kommandozeilen Werkzeug für AWS S3. AWS S3 stellt Speicherplatz in der Cloud zur Verfügung.
> Mehr Informationen: <https://aws.amazon.com/cli>.

- Auflistung aller Objekte in einem Bucket:

`aws s3 ls {{bucket_name}}`

- Synchronisieren von Dateien und Verzeichnissen zu einem Bucket:

`aws s3 sync {{path/to/files}} s3://{{bucket_name}}`

- Synchronisieren von Dateien und Verzeichnissen von einem Bucket:

`aws s3 sync s3://{{bucket_name}} {{path/to/target}}`

- Synchronisieren von Dateien und Verzeichnissen mit Ausnahmen:

`aws s3 sync {{path/to/files}} s3://{{bucket_name}} --exclude {{path/to/file}} --exclude {{path/to/directory}}/*`

- Entfernen eines Objektes von einem Bucket:

`aws s3 rm s3://{{bucket}}/{{path/to/file}}`

- Probelauf eines angegeben Kommandos ohne diesen auszuführen:

`aws s3 {{any_command}} --dryrun`

# rclone

> program CLI pentru copiere/sincronizare/mutare fișiere și directoare în și din multe servicii cloud.
> Mai multe informaţii: <https://rclone.org>

- Lista conținutului unui director pe o telecomandă rclone:

`rclone lsf {{remote_name}}:{{path/to/directory}}`

- Copiați fișierul sau directorul de la sursa locală la destinație de la distanță:

`rclone copy {{path/to/source_file_or_directory}} {{remote_name}}:{{path/to/destination_directory}}`

- Copiați fișierul sau directorul de la sursă la distanță la destinație locală:

`rclone copy {{remote_name}}:{{path/to/source_file_or_directory}} {{path/to/destination_directory}}`

- Sincronizați sursa locală cu destinația de la distanță, schimbând doar destinația:

`rclone sync {{path/to/file_or_directory}} {{remote_name}}:{{path/to/directory}}`

- Mutați fișierul sau directorul de la sursa locală la destinație de la distanță:

`rclone move {{path/to/file_or_directory}} {{remote_name}}:{{path/to/directory}}`

- Ștergeți fișierul sau directorul de la distanță (utilizați `—dry-run` pentru a testa, eliminați-l pentru a șterge efectiv):

`rclone --dry-run delete {{remote_name}}:{{path/to/file_or_directory}}`

- Mount rclone la distanță (experimental):

`rclone mount {{remote_name}}:{{path/to/directory}} {{path/to/mount_point}}`

- Demontați rclone la distanță dacă CTRL-C nu reușește (experimental):

`fusermount -u {{path/to/mount_point}}`

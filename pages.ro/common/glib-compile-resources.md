# glib-compile-resources

> Compilează fișierele de resurse (de exemplu, imagini) într-un pachet de resurse binare.
> Acestea pot fi legate de aplicațiile GTK utilizând API-ul GRESource.
> Mai multe informaţii: <https://manned.org/glib-compile-resources>

- Compilarea resurselor la care se face referire în `file.gresource.xml` la un binar .gresource:

`glib-compile-resources {{file.gresource.xml}}`

- Compilarea resurselor menționate în `file.gresource.xml` într-un fișier sursă C:

`glib-compile-resources --generate-source {{file.gresource.xml}}`

- Compilarea resurselor în `file.gresource.xml` într-un fișier țintă ales, cu extensia `.c`, `.h` sau `.gresource`:

`glib-compile-resources --generate --target={{file.ext}} {{file.gresource.xml}}`

- Imprimați o listă de fișiere de resurse la care se face referire în `file.gresource.xml`:

`glib-compile-resources --generate-dependencies {{file.gresource.xml}}`

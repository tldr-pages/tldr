# realpath

> Toon het opgeloste absolute pad voor een bestand of map.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/realpath-invocation.html>.

- Toon het absolute pad voor een bestand of map:

`realpath {{pad/naar/bestand_of_map}}`

- Vereis dat alle padcomponenten bestaan:

`realpath {{[-e|--canonicalize-existing]}} {{pad/naar/bestand_of_map}}`

- Los ".." componenten op voordat symlinks worden gevolgd:

`realpath {{[-L|--logical]}} {{pad/naar/bestand_of_map}}`

- Schakel symlink-uitbreiding uit:

`realpath {{[-s|--no-symlinks]}} {{pad/naar/bestand_of_map}}`

- Onderdruk foutmeldingen:

`realpath {{[-q|--quiet]}} {{pad/naar/bestand_of_map}}`

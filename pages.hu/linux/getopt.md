# getopt

> Parse command line arguments. További információ: <https://www.gnu.org/software/libc/manual/html_node/Getopt.html>.

- Az opcionális `verbose`/`version` jelzők elemzése rövidítésekkel:

`getopt --options vV --longoptions verbose,version -- --version --verbose`

- Adjon hozzá egy `--file` opciót egy kötelező argumentummal a `-f` rövidítéssel:

`getopt --options f: --longoptions file: -- --file=somefile`

- Adjon hozzá egy `--verbose` opciót egy opcionális argumentummal a `-v` rövidítéssel, és adjon át egy nem opciós paramétert: `arg`:

`getopt --options v:: --longoptions verbose:: -- --verbose arg`

- A `-r` és a `--verbose` zászló, egy opcionális argumentummal rendelkező `--accept` opció elfogadása és egy kötelező argumentummal rendelkező `--target` opció hozzáadása gyorsírással:

`getopt --options rv::s::t: --longoptions verbose,source::,target: -- -v --target target`

# test

> Controleer bestandstypen en vergelijk waarden.
> Retourneert 0 als de voorwaarde waar is, 1 als de voorwaarde onwaar is.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/test-invocation.html>.

- Test of een gegeven variabele gelijk is aan een gegeven string:

`test "{{$MY_VAR}}" = "{{/bin/zsh}}"`

- Test of een gegeven variabele leeg is:

`test -z "{{$GIT_BRANCH}}"`

- Test of een bestand bestaat:

`test -f "{{pad/naar/bestand_of_map}}"`

- Test of een map niet bestaat:

`test ! -d "{{pad/naar/map}}"`

- Als A waar is, voer dan B uit, of C in het geval van een fout (let op dat C mogelijk wordt uitgevoerd, zelfs als A mislukt):

`test {{voorwaarde}} && {{echo "true"}} || {{echo "false"}}`

- Gebruik `test` in een conditioneel statement:

`if test -f "{{pad/naar/bestand}}"; then echo "File exists"; else echo "File does not exist"; fi`

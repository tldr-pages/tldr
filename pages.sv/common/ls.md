# ls

> Lista innehåll i en mapp.
> Mer information: <https://www.gnu.org/software/coreutils/manual/html_node/ls-invocation.html>.

- Lista filer radvis:

`ls -1`

- Lista alla filer, inklusive dolda filer:

`ls {{[-a|--all]}}`

- Lista filer med en avslutande symbol för att indikera filtyp (mapp/, symbolisk_länk@, körbar fil*, ...):

`ls {{[-F|--classify]}}`

- Lista alla filer i det [l]ånga formatet (behörigheter, ägare, storlek och ändringsdatum):

`ls {{[-la|-l --all]}}`

- Lista filer i det [l]ånga formatet med storlek i läsbara enheter (KiB, MiB, GiB):

`ls {{[-lh|-l --human-readable]}}`

- Lista filer i det [l]ånga formatet, sorterade efter [S]torlek (fallande) rekursivt:

`ls {{[-lSR|-lS --recursive]}}`

- Lista filer i det [l]ånga formatet, sorterade efter [t]id (senast ändrad först) i omvänd ordning (äldst först):

`ls {{[-ltr|-lt --reverse]}}`

- Lista endast mappar:

`ls {{[-d|--directory]}} */`

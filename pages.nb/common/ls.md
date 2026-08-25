# ls

> List opp innholdet i en mappe.
> Mer informasjon: <https://www.gnu.org/software/coreutils/manual/html_node/ls-invocation.html>.

- List filer én per linje:

`ls -1`

- List alle filer, inkludert skjulte filer:

`ls {{[-a|--all]}}`

- List filer med et etterstilt symbol som angir filtype (mappe/, symbolsk_lenke@, kjørbar*, ...):

`ls {{[-F|--classify]}}`

- List alle filer i [l]angt format (rettigheter, eierskap, størrelse og endringsdato):

`ls {{[-la|-l --all]}}`

- List filer i [l]angt format med størrelse vist i lesbare enheter (KiB, MiB, GiB):

`ls {{[-lh|-l --human-readable]}}`

- List filer i [l]angt format, sortert etter [S]tørrelse (synkende) rekursivt:

`ls {{[-lSR|-lS --recursive]}}`

- List filer i [l]angt format, sortert etter [t]idspunkt for siste endring og i omvendt rekkefølge (eldste først):

`ls {{[-ltr|-lt --reverse]}}`

- List kun mapper:

`ls {{[-d|--directory]}} */`

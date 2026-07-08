# aa-mergeprof

> Unisce file di profili di sicurezza AppArmor nella directory dei profili.
> Maggiori informazioni: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-mergeprof.8>.

- Unisce uno o più file di profili nella directory predefinita:

`sudo aa-mergeprof {{file1 file2 ...}}`

- Unisce file di profili in una directory specifica:

`sudo aa-mergeprof {{[-d|--dir]}} /{{path/to/profiles}} {{file1 file2 ...}}`

- Mostra aiuto:

`aa-mergeprof {{[-h|--help]}}`

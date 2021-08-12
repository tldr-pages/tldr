# numfmt

> Conversia numerelor în și din șiruri care pot fi citite de om.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/numfmt>

- Conversia 1.5K (Unități SI) la 1500:

`numfmt --from={{si}} {{1.5K}}`

- Convertiți câmpul 5 (1 indexat) în unități IEC fără a converti antet:

`ls -l | numfmt --header={{1}} --field={{5}} --to={{iec}}`

- Conversia la unități IEC, pad cu 5 caractere, aliniate la stânga:

`du -s * | numfmt --to={{iec}} --format="{{%-5f}}"`

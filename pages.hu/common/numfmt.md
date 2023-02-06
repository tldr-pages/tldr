# numfmt

> Számok konvertálása ember által olvasható karakterláncokba és karakterláncokból. További információ: <https://www.gnu.org/software/coreutils/numfmt>.

- 1.5K (SI egységek) átváltása 1500-ra:

`numfmt --from={{si}} {{1.5K}}`

- Az 5. mező (1-indexált) IEC-egységekké konvertálása a fejléc konvertálása nélkül:

`ls -l | numfmt --header={{1}} --field={{5}} --to={{iec}}`

- Konvertálás IEC-egységekké, 5 karakterrel kitöltve, balra igazítva:

`du -s * | numfmt --to={{iec}} --format="{{%-5f}}"`

# diffstat

> Hisztogram létrehozása a `diff` parancs kimenetéből. További információ: <https://manned.org/diffstat>.

- A változások megjelenítése a hisztogramban:

`diff {{file1}} {{file2}} | diffstat`

- A beillesztett, törölt és módosított változások táblázatos megjelenítése:

`diff {{file1}} {{file2}} | diffstat -t`

# pr

> Fájlok oldalszámozása vagy oszlopozása nyomtatáshoz. További információ: <https://www.gnu.org/software/coreutils/pr>.

- Több fájl nyomtatása alapértelmezett fejléccel és lábléccel:

`pr {{file1}} {{file2}} {{file3}}`

- Nyomtatás egyéni központosított fejléccel:

`pr -h "{{header}}" {{file1}} {{file2}} {{file3}}`

- Nyomtatás számozott sorokkal és egyéni dátumformátummal:

`pr -n -D "{{format}}" {{file1}} {{file2}} {{file3}}`

- Az összes fájl együttes nyomtatása, egy-egy oszlopban, fejléc és lábléc nélkül:

`pr -m -T {{file1}} {{file2}} {{file3}}`

- Nyomtatás a 2. oldaltól kezdve az 5. oldalig, adott oldalhosszal (fejléccel és lábléccel együtt):

`pr +{{2}}:{{5}} -l {{page_length}} {{file1}} {{file2}} {{file3}}`

- Nyomtatás minden sorhoz eltolással és csonkoló egyéni oldalszélességgel:

`pr -o {{offset}} -W {{width}} {{file1}} {{file2}} {{file3}}`

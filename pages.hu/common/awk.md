# awk

> Egy sokoldalú programozási nyelv a fájlokkal való munkához. További információ: <https://github.com/onetrueawk/awk>.

- Az ötödik oszlop (más néven mező) nyomtatása egy szóközzel elválasztott fájlban:

`awk '{print $5}' {{path/to/file}}`

- A "foo" szót tartalmazó sorok második oszlopának nyomtatása egy szóközzel elválasztott fájlban:

`awk '/{{foo}}/ {print $2}' {{path/to/file}}`

- Nyomtassa ki egy fájl minden sorának utolsó oszlopát, vesszőt használva (szóköz helyett) mezőelválasztóként:

`awk -F ',' '{print $NF}' {{path/to/file}}`

- Egy fájl első oszlopának értékeinek összegzése és az összeg kiírása:

`awk '{s+=$1} END {print s}' {{path/to/file}}`

- Minden harmadik sor nyomtatása az első sortól kezdődően:

`awk 'NR%3==1' {{path/to/file}}`

- Különböző értékek nyomtatása feltételek alapján:

`awk '{if ($1 == "foo") print "Exact match foo"; else if ($1 ~ "bar") print "Partial match bar"; else print "Baz"}' {{path/to/file}}`

- Minden olyan sor nyomtatása, ahol a 10. oszlop értéke megegyezik a megadott értékkel:

`awk '($10 == value)'`

- Az összes olyan sor kiírása, amelyben a 10. oszlop értéke egy min és egy max érték között van:

`awk '($10 >= min_value && $10 <= max_value)'`

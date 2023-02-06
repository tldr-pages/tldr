# keybase

> Kulcskönyvtár, amely a közösségi média identitásokat nyilvánosan ellenőrizhető módon hozzárendeli a titkosítási kulcsokhoz. További információ: <https://keybase.io/docs/command_line>.

- Kövessen egy másik felhasználót:

`keybase follow {{username}}`

- Új bizonyíték hozzáadása:

`keybase prove {{service}} {{service_username}}`

- Fájl aláírása:

`keybase sign --infile {{input_file}} --outfile {{output_file}}`

- Aláírt fájl ellenőrzése:

`keybase verify --infile {{input_file}} --outfile {{output_file}}`

- Egy fájl titkosítása:

`keybase encrypt --infile {{input_file}} --outfile {{output_file}} {{receiver}}`

- Fájl visszafejtése:

`keybase decrypt --infile {{input_file}} --outfile {{output_file}}`

- Az aktuális eszköz visszavonása, kijelentkezés és a helyi adatok törlése:

`keybase deprovision`

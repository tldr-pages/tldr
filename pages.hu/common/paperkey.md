# paperkey

> OpenPGP kulcsarchiváló. További információ: <https://www.jabberwocky.com/software/paperkey/>.

- Vegyen egy adott titkos kulcsot, és generáljon egy szöveges fájlt a titkos adatokkal:

`paperkey --secret-key {{path/to/secret_key.gpg}} --output {{path/to/secret_data.txt}}`

- Vegyük a titkos kulcs adatait a `secret_data.txt` oldalon, és kombináljuk a nyilvános kulccsal a titkos kulcs rekonstruálásához:

`paperkey --pubring {{path/to/public_key.gpg}} --secrets {{path/to/secret_data.txt}} --output {{secret_key.gpg}}`

- Exportáljon egy adott titkos kulcsot, és hozzon létre egy szöveges fájlt a titkos adatokkal:

`gpg --export-secret-key {{key}} | paperkey --output {{path/to/secret_data.txt}}`

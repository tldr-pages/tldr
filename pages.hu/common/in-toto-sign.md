# in-toto-sign

> Jelentkezzen be a link vagy az elrendezés metaadataiba, vagy ellenőrizze az aláírásokat. További információ: <https://in-toto.readthedocs.io/en/latest/command-line-tools/in-toto-sign.html>.

- Írja alá az 'unsigned.layout' állományt két kulccsal, és írja a 'root.layout' állományba:

`in-toto-sign -f {{unsigned.layout}} -k {{priv_key1}} {{priv_key2}} -o {{root.layout}}`

- Az aláírás kicserélése a linkfájlban és írása az alapértelmezett fájlnévre:

`in-toto-sign -f {{package.2f89b927.link}} -k {{priv_key}}`

- 3 kulccsal aláírt elrendezés ellenőrzése:

`in-toto-sign -f {{root.layout}} -k {{pub_key0}} {{pub_key1}} {{pub_key2}} --verify`

- Aláír egy elrendezést az alapértelmezett GPG kulccsal az alapértelmezett GPG kulcstárban:

`in-toto-sign -f {{root.layout}} --gpg`

- A '...439F3C2' kulcsazonosítóval azonosított GPG-kulccsal készült elrendezés ellenőrzése:

`in-toto-sign -f {{root.layout}} --verify --gpg {{...439F3C2}}`

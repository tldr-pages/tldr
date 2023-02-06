# security

> Kulcstartók, kulcsok, tanúsítványok és a biztonsági keretrendszer kezelése. További információ: <https://ss64.com/osx/security.html>.

- Az összes elérhető kulcstartó listázása:

`security list-keychains`

- Egy adott kulcstár törlése:

`security delete-keychain {{path/to/file.keychain}}`

- Kulcstár létrehozása:

`security create-keychain -p {{password}} {{path/to/file.keychain}}`

- Tanúsítvány beállítása egy weboldal vagy \[s\]ervice használatához a \[c\]ommon név alapján (sikertelen, ha több azonos közös nevű tanúsítvány létezik):

`security set-identity-preference -s {{URL|hostname|service}} -c "{{common_name}}" {{path/to/file.keychain}}`

- Tanúsítvány hozzáadása fájlból egy \[k\]eychainhoz (ha a -k nincs megadva, az alapértelmezett kulcsláncot használja a rendszer):

`security add-certificates -k {{file.keychain}} {{path/to/cert.pem}}`

- CA-tanúsítvány hozzáadása a felhasználónkénti bizalmi beállításokhoz:

`security add-trusted-cert -k {{path/to/user-keychain.keychain-db}} {{path/to/ca-cert.pem}}`

- CA-tanúsítvány eltávolítása a felhasználónkénti bizalmi beállításokból:

`security remove-trusted-cert {{path/to/ca-cert.pem}}`

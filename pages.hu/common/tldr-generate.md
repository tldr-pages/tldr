# tlmgr generate

> Konfigurációs fájlok újraalkotása helyben tárolt információkból. További információ: <https://www.tug.org/texlive/tlmgr.html>.

- A konfigurációs fájl egy adott helyre történő tárolásának újraalkotása:

`tlmgr generate --dest {{output_file}}`

- A konfigurációs fájl újraalkotása egy helyi konfigurációs fájl felhasználásával:

`tlmgr generate --localcfg {{local_configuration_file}}`

- Futtassa a szükséges programokat a konfigurációs fájlok újraépítése után:

`tlmgr generate --rebuild-sys`

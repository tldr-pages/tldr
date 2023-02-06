# azcopy

> Fájlátviteli eszköz Azure Cloud Storage fiókokba történő feltöltéshez. További információ: <https://learn.microsoft.com/azure/storage/common/storage-use-azcopy-v10>.

- Jelentkezzen be egy Azure bérlőbe:

`azopy login`

- Helyi fájl feltöltése:

`azcopy copy '{{path/to/source/file}}' 'https://{{storage_account_name}}.blob.core.windows.net/{{container_name}}/{{blob_name}}'`

- Fájlok feltöltése `.txt` és `.jpg` kiterjesztéssel:

`azcopy copy '{{path/to/source}}' 'https://{{storage_account_name}}.blob.core.windows.net/{{container_name}}' --include-pattern '{{*.txt;*.jpg}}'`

- Konténer másolása közvetlenül két Azure tárolófiók között:

`azcopy copy 'https://{{source_storage_account_name}}.blob.core.windows.net/{{container_name}}' 'https://{{destination_storage_account_name}}.blob.core.windows.net/{{container_name}}'`

- Helyi könyvtár szinkronizálása és fájlok törlése a célállomáson, ha azok már nem léteznek a forrásban:

`azcopy sync '{{path/to/source}}' 'https://{{storage_account_name}}.blob.core.windows.net/{{container_name}}' --recursive --delete-destination=true`

- Részletes használati információk megjelenítése:

`azcopy --help`

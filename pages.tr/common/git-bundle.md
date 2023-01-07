# git bundle

> Cisim ve referansları bir arşive paketle.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-bundle>.

- Belirtilmiş bir dalın tüm cisim ve referanslarını içeren bir paket dosyası oluştur:

`git bundle create {{örnek/dosyas.bundle}} {{dal_ismi}}`

- Tüm dallar için bir paket dosyası oluştur:

`git bundle create {{örnek/dosyas.bundle}} --all`

- Mevcut daldaki en son 5 commit için bir paket dosyası oluştur:

`git bundle create {{örnek/dosya.bundle}} -{{5}} {{HEAD}}`

- Son 7 günü içeren bir paket dosyası oluştur:

`git bundle create {{örnek/dosya.bundle}} --since={{7.days}} {{HEAD}}`

- Bir paket dosyasının geçerli olduğunu ve mevcut depoya uygulanabileceğini doğrula:

`git bundle verify {{örnek/dosya.bundle}}`

- Bir pakette bulunan referansları sırala:

`git bundle unbundle {{örnek/dosya.bundle}}`

- Belirtilen dalı paket dosyasından çıkarıp mevcut depoya koy:

`git pull {{örnek/dosya.bundle}} {{dal_ismi}}`

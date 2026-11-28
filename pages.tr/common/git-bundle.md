# git bundle

> Cisim ve referansları bir arşive paketle.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-bundle>.

- Belirtilmiş bir dalın tüm cisim ve referanslarını içeren bir paket dosyası oluştur:

`git bundle create {{yol/dosya.bundle}} {{dal_ismi}}`

- Tüm dallar için bir paket dosyası oluştur:

`git bundle create {{yol/dosya.bundle}} --all`

- Mevcut daldaki en son 5 commit için bir paket dosyası oluştur:

`git bundle create {{yol/dosya.bundle}} -5 {{HEAD}}`

- Son 7 günü içeren bir paket dosyası oluştur:

`git bundle create {{yol/dosya.bundle}} --since 7.days {{HEAD}}`

- Bir paket dosyasının geçerli olduğunu ve mevcut depoya uygulanabileceğini doğrula:

`git bundle verify {{yol/dosya.bundle}}`

- Bir pakette bulunan referansların listesini `stdout`'a yazdır:

`git bundle unbundle {{yol/dosya.bundle}}`

- Belirtilen dalı paket dosyasından çıkarıp mevcut depoya koy:

`git pull {{yol/dosya.bundle}} {{dal_ismi}}`

- Bir paketten yeni bir depo oluştur:

`git clone {{yol/dosya.bundle}}`

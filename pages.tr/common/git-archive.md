# git archive

> İsimlendirilmiş bir ağaçtan dosyaların arşivini oluştur.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-archive>.

- Mevcut HEAD'deki içerik ile bir tar arşivi oluştur ve içeriği standart çıktı biçiminde göster:

`git archive --verbose HEAD`

- Mevcut HEAD'deki içerik ile bir zip arşivi oluştur ve içeriği standart çıktı biçiminde göster:

`git archive --verbose --format zip HEAD`

- Yukarıda yazan madde ile aynı şeyi yap, ama zip arşivini belirtilen dosya olarak yaz:

`git archive --verbose --output {{örnek/arşiv/dosyası.zip}} HEAD`

- Belirtilmiş bir daldaki son commitlerin içeriğinden bir tar arşivi oluştur:

`git archive --output {{örnek/arşiv/dosyası.tar}} {{dal_ismi}}`

- Belirtilmiş bir dizindeki içeriklerden tar arşivi oluştur:

`git archive --output {{örnek/arşiv/dosyası.tar}} HEAD:{{örnek/dizin}}`

- Bir takım dosyayı belirtilmiş bir dizinin içinde arşivlemek için başlarına yol ekle:

`git archive --output {{örnek/arşiv/dosyası.tar}} --prefix {{başlarına/yol/eklenecek/dosyalar}}/ HEAD`

# git commit

> Depoya dosya commit'le.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-commit>.

- Bir düzenleyici aç, mesajı yaz ve sahnelenmiş dosyaları depoya commit'le:

`git commit`

- Sahnelenmiş dosyaları belirtilen mesaj ile depoya commit'le:

`git commit {{[-m|--message]}} "{{mesaj}}"`

- Sahnelenmiş dosyaları, mesajı bir dosyadan okuyarak commit'le:

`git commit {{[-F|--file]}} {{yol/commit_mesajı_dosyası}}`

- Değiştirilmiş ve silinmiş tüm dosyaları otomatik olarak sahnele ve commit'le:

`git commit {{[-a|--all]}} {{[-m|--message]}} "{{mesaj}}"`

- Sahnelenmiş dosyaları commit'le ve belirtilen GPG anahtarı ile imzala (`anahtar_kimliği` belirtilmezse yapılandırma dosyasında tanımlı olan kullanılır):

`git commit {{[-S|--gpg-sign=]}}{{anahtar_kimliği}} {{[-m|--message]}} "{{mesaj}}"`

- Şu anda sahnelenmiş değişiklikleri ekleyerek son commit'i güncelle (commit'in hash'i değişir) ve mesajı değiştirmek için bir düzenleyici aç:

`git commit --amend`

- Yalnızca belirtilmiş (halihazırda sahnelenmiş) dosyaları commit'le:

`git commit {{yol/dosya1 yol/dosya2 ...}}`

- Belirtilen mesaj ve açıklama ile bir commit oluştur:

`git commit {{[-m|--message]}} "{{mesaj}}" {{[-m|--message]}} "{{açıklama}}"`

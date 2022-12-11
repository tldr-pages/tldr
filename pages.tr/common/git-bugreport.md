# git bugreport

> Sşstem ve kullanıcıdan hata ayıklama bilgisi çeker ve olası bir Git hatasının rapor edilmesi için bu bilgiyi oluşturduğu bir metin dosyasına kaydeder.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-bugreport>.

- Mevcut dizinde yeni bir hata rapor dosyası oluştur:

`git bugreport`

- Belirtilen dizinde yeni bir hata rapor dosyası oluştur:

`git bugreport --output-directory {{örnek/dizin}}`

- `strftime` formatında belirtilmiş bir dosya adı ekiyle yeni bir rapor dosyası oluştur:

`git bugreport --suffix {{%m%d%y}}`

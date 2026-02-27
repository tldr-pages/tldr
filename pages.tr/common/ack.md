# ack

> Geliştiriciler için optimize edilmiş, `grep` benzeri bir arama aracı.
> Ayrıca bakınız: `rg`.
> Daha fazla bilgi için: <https://beyondgrep.com/documentation/>.

- Geçerli dizinde özyinelemeli olarak bir dize veya `regex` içeren dosyaları ara:

`ack "{{aranacak_desen}}"`

- Büyük/küçük harf duyarsız bir desen ara:

`ack {{[-i|--ignore-case]}} "{{aranacak_desen}}"`

- Bir desenle eşleşen satırları ara, sadece eşleşen metni yazdır (satırın geri kalanını değil):

`ack {{[-o|--output '$&']}} "{{aranacak_desen}}"`

- Aramayı belirli bir dosya türüyle sınırla:

`ack {{[-t|--type]}} {{ruby}} "{{aranacak_desen}}"`

- Belirli bir dosya türündeki dosyalarda arama yapma:

`ack {{[-t|--type]}} no{{ruby}} "{{aranacak_desen}}"`

- Bulunan toplam eşleşme sayısını say:

`ack {{[-c|--count]}} {{[-h|--no-filename]}} "{{aranacak_desen}}"`

- Sadece dosya adlarını ve her dosya için eşleşme sayısını yazdır:

`ack {{[-c|--count]}} {{[-l|--files-with-matches]}} "{{aranacak_desen}}"`

- `--type` ile kullanılabilecek tüm değerleri listele:

`ack --help-types`

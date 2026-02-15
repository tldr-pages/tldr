# ack

> Geliştiriciler için optimize edilmiş, `grep` benzeri bir arama aracı.
> Ayrıca bakınız: `rg`.
> Daha fazla bilgi için: <https://beyondgrep.com/documentation/>.

- Geçerli dizinde özyinelemeli olarak bir dize veya `regex` içeren dosyaları ara:

`ack "{{aranacak_desen}}"`

- Büyük/küçük harf duyarsız bir desen ara:

`ack {{--ignore-case}} "{{aranacak_desen}}"`

- Bir desenle eşleşen satırları ara, sadece eşleşen metni yazdır (satırın geri kalanını değil):

`ack --output '$&' "{{aranacak_desen}}"`

- Aramayı belirli bir dosya türüyle sınırla:

`ack --type {{ruby}} "{{aranacak_desen}}"`

- Belirli bir dosya türündeki dosyalarda arama yapma:

`ack --type no{{ruby}} "{{aranacak_desen}}"`

- Bulunan toplam eşleşme sayısını say:

`ack --count --no-filename "{{aranacak_desen}}"`

- Sadece dosya adlarını ve her dosya için eşleşme sayısını yazdır:

`ack --count --files-with-matches "{{aranacak_desen}}"`

- `--type` ile kullanılabilecek tüm değerleri listele:

`ack --help-types`

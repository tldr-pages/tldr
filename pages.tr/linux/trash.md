# trash

> Çöp / geri dönüşüm kutusunu yönetmek için bir komut satırı arayüzü.
> Daha fazla bilgi için: <https://github.com/andreafrancia/trash-cli>.

- Bir dosyayı sil (çöpe gönder):

`trash {{örnek/dosya}}`

- Çöpteki dosyaları göster:

`trash-list`

- Çöpteki dosyaları geri getir:

`trash-restore`

- Çöpü boşalt:

`trash-empty`

- Çöpü 10 gün öncesinden daha yeni atılan dosyalar hariç boşalt:

`trash-empty {{10}}`

- Çöpte 'foo' ismini taşıyan tüm dosyaları sil:

`trash-rm "foo"`

- Belirtilen konumdaki tüm dosyaları sil:

`trash-rm {{/detaylı/örnek/konum/dosya_veya_dizin}}`

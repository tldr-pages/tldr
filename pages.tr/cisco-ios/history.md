# history

> Komut satırı geçmişini yönet.
> Daha fazla bilgi için: <https://www.gnu.org/software/bash/manual/bash.html#index-history>.

- Komut geçmişi listesini satır numaralarıyla göster:

`history`

- Son 20 komutu göster (Zsh'de 20. komuttan itibaren tüm komutları gösterir):

`history 20`

- Geçmişi farklı biçimlerde zaman damgalarıyla göster (yalnızca Zsh'de kullanılabilir):

`history -{{d|f|i|E}}`

- Komut geçmişi listesini temizle:

`history -c`

- Geçmiş dosyasının üzerine geçerli Bash kabuğunun geçmişini yaz (geçmişi tamamen silmek için genellikle `history -c` ile birlikte kullanılır):

`history -w`

- Belirtilen konumdaki geçmiş kaydını sil:

`history -d {{konum}}`

- Bir komutu çalıştırmadan geçmişe ekle:

`history -s {{komut}}`

- Başına boşluk ekleyerek bir komutu geçmişe eklemeden çalıştır:

`<Space>{{komut}}`

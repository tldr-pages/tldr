# alias

> Takma adlar/kısayollar (bir komut dizesi ile değiştirilen sözcükler) oluşturur.
> Kısayollar, kabuğun yapılandırma dosyasında (örneğin `~/.bashrc`) tanımlanmadığı sürece geçerli kabuk oturumuyla birlikte sona erer.
> Daha fazla bilgi için: <https://tldp.org/LDP/abs/html/aliases.html>.

- Tüm kısayolları listele:

`alias`

- Genel bir kısayol oluştur:

`alias {{kelime}}="{{komut}}"`

- Bir kısayolun verildigi komutu göster:

`alias {{kelime}}`

- Bir kısayolu kaldır:

`unalias {{kelime}}`

- `rm`'yi interaktif bir komuta dönüştür:

`alias {{rm}}="{{rm --interactive}}"`

- `la`'yi `ls --all` için kısayol olarak oluştur:

`alias {{la}}="{{ls --all}}"`

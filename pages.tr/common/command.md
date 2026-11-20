# command

> Kabuğun aynı adlı fonksiyonları, yerleşik komutları ve takma adları yoksayarak programı çalıştırmasını zorla.
> Daha fazla bilgi için: <https://www.gnu.org/software/bash/manual/bash.html#index-command>.

- Aynı adlı bir takma ad olsa bile `ls` programını doğrudan çalıştır:

`command ls`

- Tüm standart yardımcı programları bulmayı garanti eden varsayılan bir `$PATH` (`/bin:/usr/bin:/sbin:/usr/sbin:/etc:/usr/etc`) kullanarak bir komutu bul ve çalıştır:

`command -p {{komut}}`

- Belirli bir komutun çalıştırılabilir dosyasının yolunu veya takma ad tanımını göster:

`command -v {{komut}}`

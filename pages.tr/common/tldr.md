# tldr

> Komut satırı araçları için tldr-pages projesinden basit yardım sayfaları görüntüler.
> Not: `--language` ve `--list` seçenekleri istemci spesifikasyonunda zorunlu değildir, ancak çoğu istemci bunları destekler.
> Ayrıca bakınız: `cheatshh`, `cheat`, `navi`.
> Daha fazla bilgi için: <https://github.com/tldr-pages/tldr/blob/main/CLIENT-SPECIFICATION.md#command-line-interface>.

- Belirli bir komutun tldr sayfasını göster (ipucu: burayı görüntülemek için kullandığınız komutun aynısı!):

`tldr {{komut}}`

- Belirli bir alt komutun tldr sayfasını göster:

`tldr {{komut}} {{alt_komut}}`

- Bir komutun tldr sayfasını belirtilen dilde göster (varsa; yoksa İngilizce sayfayı göster):

`tldr {{[-L|--language]}} {{dil_kodu}} {{komut}}`

- Bir komutun belirli bir platformdaki tldr sayfasını göster:

`tldr {{[-p|--platform]}} {{android|cisco-ios|common|dos|freebsd|linux|netbsd|openbsd|osx|sunos|windows}} {{komut}}`

- tldr sayfalarının yerel önbelleğini güncelle:

`tldr {{[-u|--update]}}`

- Mevcut platform ve `common` için tüm sayfaları listele:

`tldr {{[-l|--list]}}`

- Bir komutun tldr sayfasını kısa seçenekleri göstererek görüntüle:

`tldr --short-options {{komut}}`

- tldr sayfalarına bir terminal penceresinde göz at (`fzf` kurulu olmalı):

`tldr {{[-l|--list]}} | fzf --preview "tldr {1} --color=always" --preview-window=right,70% | xargs tldr`

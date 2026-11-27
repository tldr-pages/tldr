# fd

> Dosya sisteminde girdileri bul.
> Ayrıca bakınız: `find`, `regex`.
> Daha fazla bilgi için: <https://github.com/sharkdp/fd#command-line-options>.

- Geçerli dizinde belirli bir desenle eşleşen dosyaları özyinelemeli olarak bul:

`fd "{{normal_ifade}}"`

- Belirli bir dizindeki dosyaları bul:

`fd "{{normal_ifade}}" {{yol/dizin}}`

- Belirli bir uzantıya sahip dosyaları bul:

`fd {{[-e|--extension]}} {{txt}}`

- Yalnızca belirli bir desenle eşleşen dizinleri bul:

`fd "{{normal_ifade}}" {{[-t|--type]}} {{[d|directory]}}`

- Yok sayılan ve gizli dosyaları da aramaya dahil et:

`fd "{{normal_ifade}}" {{[-HI|--hidden --no-ignore]}}`

- Belirli bir `glob` desenine uyan dosyaları hariç tut:

`fd "{{normal_ifade}}" {{[-E|--exclude]}} {{glob}}`

- Döndürülen her arama sonucu üzerinde bir komut çalıştır:

`fd "{{normal_ifade}}" {{[-x|--exec]}} {{komut}}`

- Yalnızca geçerli dizindeki dosyaları bul:

`fd "{{normal_ifade}}" {{[-d|--max-depth]}} 1`

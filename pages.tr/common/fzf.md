# fzf

> Komut satırı belirsiz bulucu.
> Sk'ya benzer.
> Daha fazla bilgi için: <https://github.com/junegunn/fzf>.

- Belirtilen dizindeki tüm dosyalarda FZF'yi başlat:

`find {{dosya/yolu/dizin}} -type f | fzf`

- Çalışan süreçler için FZF'yi başlat:

`ps aux | fzf`

- `Shift + Tab` ile birden çok dosya seç ve bir dosyaya yaz:

`find {{dosya/yolu/dizin}} -type f | fzf --multi > {{dosya/yolu/dosya}}`

- fzf'yi belirli bir sorgu ile başlat:

`fzf --query "{{sorgu}}"`

- Core ile başlayan ve Go, RB veya PY ile biten girişlerde fzf'yi başlat:

`fzf --query "^core go$ | rb$ | py$"`

- PYC ile eşleşmeyen ve Travis'e tam olarak eşleşen girişlerde fzf'yi başlat:

`fzf --query "!pyc 'travis"`

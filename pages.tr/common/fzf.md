# fzf

> Komut satırı belirsiz bulucu.
> Sk'ya benzer.
> Daha fazla bilgi: <https://github.com/junegunn/fzf>.

- Belirtilen dizindeki tüm dosyalarda FZF'yi başlatın:

`find {{dosya/yolu/dizin}} -type f | fzf`

- Çalışan süreçler için FZF'yi başlatın:

`ps aux | fzf`

- `Shift + Tab` ile birden çok dosya seçin ve bir dosyaya yazın:

`find {{dosya/yolu/dizin}} -type f | fzf --multi > {{dosya/yolu/dosya}}`

- fzf'yi belirli bir sorgu ile başlatın:

`fzf --query "{{sorgu}}"`

- Core ile başlayan ve Go, RB veya PY ile biten girişlerde fzf'yi başlatın:

`fzf --query "^core go$ | rb$ | py$"`

- PYC ile eşleşmeyen ve Travis'e tam olarak eşleşen girişlerde fzf'yi başlatın:

`fzf --query "!pyc 'travis"`

# clear

> Terminal ekranını temizle.
> Daha fazla bilgi için: <https://manned.org/clear>.

- Ekranı temizle:

`clear`

- Ekranı temizle ancak terminalin geri kaydırma arabelleğini koru (Bash'te `<Ctrl l>` tuşlarına basmaya eşdeğerdir):

`clear -x`

- Temizlenecek terminal türünü belirt (varsayılan olarak `$TERM` ortam değişkeninin değeri kullanılır):

`clear -T {{terminal_türü}}`

- `clear` tarafından kullanılan `ncurses` sürümünü göster:

`clear -V`

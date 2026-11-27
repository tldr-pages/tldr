# git apply

> İndeks veya dosyalara yama uygula.
> Ayrıca bakınız: `git am`.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-apply>.

- Yamalanan dosyalarla ilgili mesajları yazdır:

`git apply {{[-v|--verbose]}} {{yol/dosya}}`

- Yamalanan dosyaları indekse uygula ve ekle:

`git apply --index {{yol/dosya}}`

- Uzak yama dosyası uygula:

`curl {{[-L|--location]}} {{https://example.com/dosya.patch}} | git apply`

- Çıktı için fark statistiği çıkar ve yamayı uygula:

`git apply --stat --apply {{yol/dosya}}`

- Yamayı tersten uygula:

`git apply {{[-R|--reverse]}} {{yol/dosya}}`

- Yama sonucunu çalışan ağacı değiştirmeden indekste sakla:

`git apply --cached {{yol/dosya}}`

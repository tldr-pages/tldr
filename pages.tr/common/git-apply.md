# git apply

> İndeks veya dosyalara yama uygula.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-apply>.

- Yamalanan dosyalarla ilgili mesajları yazdır:

`git apply {{[-v|--verbose]}} {{örnek/dosya}}`

- Yamalanan dosyaları indekse uygula ve ekle:

`git apply --index {{örnek/dosya}}`

- Uzak yama dosyası uygula:

`curl {{[-L|--location]}} {{https://ornek.com/dosya.patch}} | git apply`

- Çıktı için fark statistiği çıkar ve yamayı uygula:

`git apply --stat --apply {{örnek/dosya}}`

- Yamayı tersten uygula:

`git apply {{[-R|--reverse]}} {{örnek/dosya}}`

- Yama sonucunu çalışan ağacı değiştirmeden indekste sakla:

`git apply --cache {{örnek/dosya}}`

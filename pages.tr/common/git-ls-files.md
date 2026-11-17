# git ls-files

> İndex ve mevcut ağaçtaki dosyalar hakkında bilgi göster.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-ls-files>.

- Silinen dosyaları göster:

`git ls-files {{[-d|--deleted]}}`

- Düzenlenen ve silinen dosyaları göster:

`git ls-files {{[-m|--modified]}}`

- Yoksayılmış ve izlenmeyen dosyaları göster:

`git ls-files {{[-o|--others]}}`

- İzlenmeyen dosyaları göster, yoksayılmış olanları gösterme:

`git ls-files {{[-o|--others]}} --exclude-standard`

# git difftool

> Harici diff araçları kullanarak dosya değişimlerini göster. `git diff` ile aynı ayar ve argümanları destekler.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-difftool>.

- Müsait diff araçlarını göster:

`git difftool --tool-help`

- Varsayılan diff aracını birleştirmeye ayarla:

`git config --global diff.tool "{{meld}}"`

- Varsayılan diff aracını sahnelenmiş değişiklikleri göstermek için kullan:

`git difftool --staged`

- Verilen commit'den itibaren yapılmış değişiklikleri göstermek için (opendiff) kullan:

`git difftool --tool={{opendiff}} {{commit}}`

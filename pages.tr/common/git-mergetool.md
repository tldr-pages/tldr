# git mergetool

> Birleştirme sırasında yaşanan karışıklıkları çözmek için karışıklık çözücü araçları çalıştırır.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-mergetool>.

- Karışıklıkları çözmek için varsayılan birleştirme aracını başlat:

`git mergetool`

- Kullanılabilir birleştirme araçlarını sırala:

`git mergetool --tool-help`

- Belirtilen birleştirme aracını başlat:

`git mergetool --tool {{araç_ismi}}`

- Her birleştirme aracı çağrılışında harekete geçme:

`git mergetool --no-prompt`

- Özellikle grafiksel (GUI) birleştirme aracını kullan (merge.guitool değişkenine göz at):

`git mergetool --gui`

- Özellikle normal birleştirme aracını kullan (merge.guitool değişkenine göz at):

`git mergetool --no-gui`

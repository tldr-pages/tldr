# git commit-graph

> Git commit-graph dosyalarını yaz ve doğrula.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-commit-graph>.

- Dizinin yerel `.git` dizinindeki paketlenmiş commit'ler için bir commit-grafik dosyası yaz:

`git commit-graph write`

- Erişilebilen tüm commitleri içeren bir commit-grafik dosyası yaz:

`git show-ref --hash | git commit-graph write --stdin-commits`

- `HEAD`'den erişilebilenlerin yanında mevcut commit-grafik dosyasındaki tüm commit'leri içeren bir commit-grafik dosyası oluştur:

`git rev-parse {{HEAD}} | git commit-graph write --stdin-commits --append`

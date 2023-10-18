# git-imerge

> İki git dalı arasında aşamalı olarak birleştirme veya taban değiştirme işlemlerini uygula.
> Dallar arasındaki uyuşmazlıklar özel commitler ile bölüşülerek uyuşmazlıkları çözmek kolaylaştırılır.
> Daha fazla bilgi için: <https://github.com/mhagger/git-imerge>.

- imerge bazlı taban değiştirme işlemini başlat (işlemden önce tabanı değiştirilmek istenen dalı kontrol et):

`git imerge rebase {{yerine_geçilecek_dal}}`

- imerge bazlı birleştirme işlemini başlat (işlemden önce birleştirilmek istenen dalı kontrol et):

`git imerge merge {{birleştirilecek_dal}}`

- Devam eden birleştirme ve taban değiştirme işlemlerinin ASCII diagramını göster:

`git imerge diagram`

- Uyuşmazlıkları çözdükten sonra imerge işlemine devam et (önce `git add` komutu ile uyuşmayan dosyaları ekle):

`git imerge continue --no-edit`

- Tüm uyuşmazlıklar çözüldükten sonra imerge işlemini sonlandır:

`git imerge finish`

- imerge işlemini sonlandır ve belirtilen eski bir dala geri dön:

`git-imerge remove && git checkout {{eski_dal}}`

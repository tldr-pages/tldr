# git blame

> Her satırdaki dosyanın yanında en son commit değeri ve yazarını göster.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-blame>.

- Bir dosyayı, her satırında son commit değeri ve yazarı bulunacak şekilde göster:

`git blame {{yol/dosya}}`

- Bir dosyayı, her satırında son commit değeri ve yazarının e-postası bulunacak şekilde göster:

`git blame {{[-e|--show-email]}} {{yol/dosya}}`

- Bir dosyayı, belirli bir commit'teki haliyle her satırında yazar bilgisi bulunacak şekilde göster:

`git blame {{commit}} {{yol/dosya}}`

- Bir dosyayı, belirli bir commit'ten önceki haliyle her satırında yazar bilgisi bulunacak şekilde göster:

`git blame {{commit}}~ {{yol/dosya}}`

- Bir dosyayı, belirli bir satırdan başlayarak her satırında yazar bilgisi bulunacak şekilde göster:

`git blame -L {{123}} {{yol/dosya}}`

- Bir dosyanın belirli bir satır aralığını yazar bilgisiyle göster:

`git blame -L {{başlangıç_satırı}},{{bitiş_satırı}} {{yol/dosya}}`

- Bir dosyanın, verilen metinle eşleşen ilk satırdan başlayarak 10 satırını yazar bilgisiyle göster:

`git blame -L '/{{metin}}/',+10 {{yol/dosya}}`

- Bir dosyayı boşlukları ve satır taşımalarını yok sayarak yazar bilgisiyle göster:

`git blame -w -C -C -C {{yol/dosya}}`

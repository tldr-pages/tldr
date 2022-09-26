# git diff

> İzlenen dosyalara değişiklikleri göster.
> Daha fazla bilgi: <https://git-scm.com/docs/git-diff>.

- Sahnelenmemiş, commit'lenmemiş değişiklikleri göster:

`git diff`

- Sahnelenmiş olanlar da dahil olmak üzere tüm commit'lenmemiş değişiklikleri göster:

`git diff HEAD`

- Yalnızca sahnelenmiş (eklenmiş ancak commit'lenmemiş) değişiklikleri göster:

`git diff --staged`

- Belirtilen bir tarihten itibaren yapılmış tüm commit'lerdeki değişiklikleri göster:

`git diff 'HEAD@{3 months|weeks|days|hours|seconds ago}'`

- Belirtilen bir commit'ten itibaren yalnızca üzerinde değişiklik yapılmış dosyaların ismini göster:

`git diff --name-only {{commit}}`

- Belirtilen bir commit'ten itibaren yapılmış dosya oluşturma, yeniden adlandırma ve mod değişim işlemlerini göster:

`git diff --summary {{commit}}`

- Tek bir dosyayı iki dal veya commit arasında karşılaştır:

`git diff {{dal_1}}..{{dal_2}} [--] {{örnek/dosya}}`

- Mevcut daldaki farklı dosyaları başka bir daldakilerle karşılaştır:

`git diff {{dal}}:{{örnek/dosya2}} {{örnek/dosya}}`

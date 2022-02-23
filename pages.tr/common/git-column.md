# git column

> Kolonlarda veri görüntüle.
> Daha fazla bilgi: <https://git-scm.com/docs/git-column>.

- Standart çıktıyı çoklu kolonlar olarak biçimlendir:

`ls | git column --mode={{column}}`

- Standart çıktıyı maksimum `100` birim sütun genişliğinde biçimlendir:

`ls | git column --mode=column --width={{100}}`

- Standart çıktıyı maksimum `30` birimlik boşluğa sahip situnlar olacak şekilde biçimlendir:

`ls | git column --mode=column --padding={{30}}`

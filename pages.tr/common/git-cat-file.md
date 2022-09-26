# git cat-file

> Git depo cisimlerine dair içerik, tür ve boyut bilgisini sağla.
> Daha fazla bilgi: <https://git-scm.com/docs/git-cat-file>.

- HEAD commit'inin byte bazında boyutunu öğren:

`git cat-file -s HEAD`

- Belirtilen Git cisminin türünü (blob, ağaç, commit, etiket) öğren:

`git cat-file -t {{8c442dc3}}`

- Git objesinin içeriğini, türüne uygun olarak hoş şekilde yansıt:

`git cat-file -p {{HEAD~2}}`

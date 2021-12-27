# git submodule

> Alt modülleri incele, güncelle ve yönet.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-submodule>.

- Deponun belirtilen alt modüllerini indir:

`git submodule update --init --recursive`

- Bir Git deposunu alt modül olarak ekle:

`git submodule add {{depo_url'si}}`

- Bir Git deposunu alt modül olarak belirtilen dizinde ekle:

`git submodule add {{depo_url'si}} {{dizin/konumu}}`

- Tüm alt modülleri son commit'lerine güncelle:

`git submodule foreach git pull`

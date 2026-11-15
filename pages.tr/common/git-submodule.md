# git submodule

> Alt modülleri incele, güncelle ve yönet.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-submodule>.

- Mevcut alt modülleri ve her birinin çekilmiş (checkout) olduğu commit'i göster:

`git submodule`

- Deponun (`.gitmodules` dosyasında listelenen) alt modüllerini indir:

`git submodule update --init --recursive`

- Bir Git deposunu alt modül olarak ekle:

`git submodule add {{depo_url'si}}`

- Bir Git deposunu alt modül olarak belirtilen dizinde ekle:

`git submodule add {{depo_url'si}} {{yol/dizin}}`

- Tüm alt modülleri son commit'lerine güncelle:

`git submodule update --remote`

- Bir alt modülün URL'sini değiştir:

`git submodule set-url {{alt_modül/konumu}} {{yeni_url}}`

- Bir alt modülün kaydını sil (örneğin `git rm` ile depodan kaldırmadan önce):

`git submodule deinit {{alt_modül/konumu}}`

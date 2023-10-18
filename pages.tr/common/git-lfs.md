# git lfs

> Git depolarındaki büyük dosyalarla çalış.
> Daha fazla bilgi için: <https://git-lfs.github.com>.

- Git LFS'i başlat:

`git lfs install`

- Belirtilen topağa uygun dosyaları izle:

`git lfs track '{{*.bin}}'`

- Git LFS uç nokta URL'sini değiştir (LFS sunucusunun Git sunucusundan ayrı olması durumunda işlevseldir):

`git config -f .lfsconfig lfs.url {{lfs_uç_nokta_url'si}}`

- İzlenen kalıpları sırala:

`git lfs track`

- Commit'lenmiş izlenen dosyaları sırala:

`git lfs ls-files`

- Tğm Git LFS nesnelerini uzak sunucuya gönder (hatayla karşılaşma durumunda faydalıdır):

`git lfs push --all {{uzak_depo_adresi}} {{dal_ismi}}`

- Tüm Git LFS nesnelerini çek:

`git lfs fetch`

- Tüm Git LFS nesnelerini kontrol et:

`git lfs checkout`

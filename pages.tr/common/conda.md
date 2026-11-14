# conda

> Herhangi bir programlama dili için paketleri, bağımlılıkları ve ortamları yönet.
> `create` gibi bazı alt komutların kendi kullanım dokümantasyonu vardır.
> Ayrıca bakınız: `mamba`.
> Daha fazla bilgi için: <https://docs.conda.io/projects/conda/en/latest/commands/index.html>.

- Yeni bir ortam oluştur ve belirtilen paketleri bu ortama kur:

`conda create {{[-n|--name]}} {{ortam_adı}} {{python=3.9 matplotlib}}`

- Tüm ortamları listele:

`conda info {{[-e|--envs]}}`

- Bir ortamı etkinleştir:

`conda activate {{ortam_adı}}`

- Bir ortamı devre dışı bırak:

`conda deactivate`

- Bir ortamı (tüm paketleri kaldırarak) sil:

`conda remove {{[-n|--name]}} {{ortam_adı}} --all`

- Geçerli ortama paket kur:

`conda install {{python=3.4 numpy}}`

- Geçerli ortamda kurulu paketleri listele:

`conda list`

- Kullanılmayan paketleri ve önbellekleri sil:

`conda clean {{[-a|--all]}}`

# go clean

> Obje ve önbellek dosyalarını sil.
> Daha fazla bilgi için: <https://golang.org/cmd/go/#hdr-Remove_object_files_and_cached_files>.

- Hiçbir şeyi silmeden silme komutlarını yazdır:

`go clean -n`

- Yapım önbelleğini sil:Delete the build cache:

`go clean -cache`

- Tüm önbelleğe alınan test sonuçlarını sil:

`go clean -testcache`

- Modül önbelleğni sil:

`go clean -modcache`

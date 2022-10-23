# tar

> Arşivleme aracı.
> Genellikle gzip veya bzip2 gibi bir sıkıştırma yöntemiyle birleştirilir.
> Daha fazla bilgi için: <https://www.gnu.org/software/tar>.

- Bir arşiv oluşturun ve dosyaya yazın:

`tar cf {{target.tar}} {{file1}} {{file2}} {{file3}}`

- Bir gzip arşivi oluşturun ve dosyaya yazın:

`tar czf {{target.tar.gz}} {{file1}} {{file2}} {{file3}}`

- Göreceli yolları kullanarak bir gzip arşivi oluşturun:

`tar czf {{target.tar.gz}} --directory={{path/to/directory}} .`

- Sıkıştırılmış bir arşiv dosyasını geçerli dizine ayrıntılı şekilde çıkarın:

`tar xvf {{source.tar[.gz|.bz2|.xz]}}`

- Sıkıştırılmış bir arşiv dosyasını hedef dizine çıkarın:

`tar xf {{source.tar[.gz|.bz2|.xz]}} --directory={{directory}}`

- Sıkıştırılmış bir arşiv oluşturun ve sıkıştırma yöntemini seçmek için arşiv sonekini kullanın:

`tar caf {{target.tar.xz}} {{file1}} {{file2}} {{file3}}`

- Bir tar arşivinin içeriğini ayrıntılı olarak listeler:

`tar tvf {{source.tar}}`

- Şablonla eşleşen dosyaları arşivden çıkarın:

`tar xf {{source.tar}} --wildcards "{{*.html}}"`

# tar

> Arşivleme aracı.
> Genellikle gzip veya bzip2 gibi bir sıkıştırma yöntemiyle birleştirilir.
> Daha fazla bilgi: <https://www.gnu.org/software/tar>.

- Bir arşiv oluşturun ve dosyaya yazın:

`tar cf {{hedef.tar}} {{dosya1}} {{dosya2}} {{dosya3}}`

- Bir gzip arşivi oluşturun ve dosyaya yazın:

`tar czf {{hedef.tar.gz}} {{dosya1}} {{dosya2}} {{dosya3}}`

- Göreceli yolları kullanarak bir gzip arşivi oluşturun:

`tar czf {{hedef.tar.gz}} --directory={{dizin/yolu}} .`

- Sıkıştırılmış bir arşiv dosyasını geçerli dizine ayrıntılı şekilde çıkarın:

`tar xvf {{kaynak.tar[.gz|.bz2|.xz]}}`

- Sıkıştırılmış bir arşiv dosyasını hedef dizine çıkarın:

`tar xf {{kaynak.tar[.gz|.bz2|.xz]}} --directory={{dizin}}`

- Sıkıştırılmış bir arşiv oluşturun ve sıkıştırma yöntemini seçmek için arşiv sonekini kullanın:

`tar caf {{hedef.tar.xz}} {{dosya1}} {{dosya2}} {{dosya3}}`

- Bir tar arşivinin içeriğini ayrıntılı olarak listeler:

`tar tvf {{kaynak.tar}}`

- Şablonla eşleşen dosyaları arşivden çıkarın:

`tar xf {{kaynak.tar}} --wildcards "{{*.html}}"`

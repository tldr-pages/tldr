# tar

> Arşivleme aracı.
> Dosyalar genellikle gzip veya bzip2 gibi bir sıkıştırma yöntemiyle birleştirilir.
> Daha fazla bilgi için: <https://www.gnu.org/software/tar>.

- Bir arşiv oluştur ve dosyaya yaz:

`tar cf {{hedef.tar}} {{dosya1}} {{dosya2}} {{dosya3}}`

- Bir gzip arşivi oluştur ve dosyaya yaz:

`tar czf {{hedef.tar.gz}} {{dosya1}} {{dosya2}} {{dosya3}}`

- Göreceli yolları kullanarak bir gzip arşivi oluştur:

`tar czf {{hedef.tar.gz}} --directory={{dizin/yolu}} .`

- Sıkıştırılmış bir arşiv dosyasını geçerli dizine ayrıntılı şekilde çıkar:

`tar xvf {{kaynak.tar[.gz|.bz2|.xz]}}`

- Sıkıştırılmış bir arşiv dosyasını hedef dizine çıkar:

`tar xf {{kaynak.tar[.gz|.bz2|.xz]}} --directory={{dizin}}`

- Sıkıştırılmış bir arşiv oluştur ve sıkıştırma yöntemini seçmek için arşiv sonekini kullan:

`tar caf {{hedef.tar.xz}} {{dosya1}} {{dosya2}} {{dosya3}}`

- Bir tar arşivinin içeriğini ayrıntılı olarak listele:

`tar tvf {{kaynak.tar}}`

- Şablonla eşleşen dosyaları arşivden çıkar:

`tar xf {{kaynak.tar}} --wildcards "{{*.html}}"`

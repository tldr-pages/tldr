# atool

> Çeşitli biçimlerdeki arşivleri yönetin.
> Daha fazla bilgi için: <https://www.nongnu.org/atool/>.

- Bir zip arşivindeki dosyaları listele:

`atool --list {{arşiv.zip/dosyasının/yolu}}`

- Bir tar.gz arşivini yeni bir alt dizine (veya yalnızca bir dosya içeriyorsa geçerli dizine) çıkart:

`atool --extract {{arşiv.tar.gz/dosyasının/yolu}}`

- İki dosyaya sahip yeni bir 7zip arşivi oluştur:

`atool --add {{arşiv.7z/dosyasının/yolu}} {{dosya1/yolu dosya2/yolu ...}}`

- Geçerli dizindeki tüm zip ve rar arşivlerini çıkart:

`atool --each --extract {{*.zip *.rar}}`

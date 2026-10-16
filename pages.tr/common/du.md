# du

> Disk kullanımı: dosyaların ve dizinlerin kapladığı alanı tahmin et ve özetle.
> Daha fazla bilgi için: <https://www.gnu.org/software/coreutils/manual/html_node/du-invocation.html>.

- Bir dizinin ve tüm alt dizinlerinin boyutlarını verilen birimde (B/KiB/MiB) listele:

`du -{{b|k|m}} {{dizin/yolu}}`

- Bir dizinin ve tüm alt dizinlerinin boyutlarını okunabilir biçimde (yani uygun birimi otomatik seçerek) listele:

`du {{[-h|--human-readable]}} {{dizin/yolu}}`

- Tek bir dizinin boyutunu okunabilir birimlerle göster:

`du {{[-sh|--summarize --human-readable]}} {{dizin/yolu}}`

- Bir dizinin ve içindeki tüm dosya ve dizinlerin boyutlarını okunabilir biçimde listele:

`du {{[-ah|--all --human-readable]}} {{dizin/yolu}}`

- Bir dizinin ve alt dizinlerinin boyutlarını, en fazla `n` düzey derinliğe kadar okunabilir biçimde listele:

`du {{[-h|--human-readable]}} {{[-d|--max-depth]}} {{n}} {{dizin/yolu}}`

- Mevcut dizindeki tüm `.jpg` dosyalarının boyutlarını okunabilir biçimde listele ve sonunda genel toplamı göster:

`du {{[-ch|--total --human-readable]}} *.jpg`

- Belirli bir eşik boyutunun üzerindeki tüm dosya ve dizinleri (gizli olanlar dahil) listele (alanı asıl neyin kapladığını bulmak için kullanışlıdır):

`du {{[-ah|--all --human-readable]}} {{[-t|--threshold]}} {{1G|1024M|1048576K}} .[^.]* *`

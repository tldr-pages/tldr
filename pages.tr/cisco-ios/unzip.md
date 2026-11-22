# unzip

> Zip arşivlerinden dosyaları/dizinleri çıkar.
> Ayrıca bakınız: `zip`.
> Daha fazla bilgi için: <https://manned.org/unzip>.

- Belirli bir arşivdeki tüm dosyaları/dizinleri geçerli dizine çıkar:

`unzip {{yol/arşiv}}.zip`

- Bir arşivdeki dosyaları/dizinleri belirli bir dizine çıkar:

`unzip {{yol/arşiv}}.zip -d {{yol/çıktı}}`

- Bir arşivdeki dosyaları/dizinleri çıkarılan dosya adlarıyla birlikte `stdout`'a çıkar:

`unzip -c {{yol/arşiv}}.zip`

- Windows'ta oluşturulmuş, ASCII olmayan (örn. Çince veya Japonca karakterli) dosya adları içeren bir arşivi çıkar:

`unzip -O {{gbk}} {{yol/arşiv}}.zip`

- Belirli bir arşivin içeriğini çıkarmadan listele:

`unzip -l {{yol/arşiv}}.zip`

- Bir arşivden belirli dosyaları dizin yollarını yok sayarak geçerli dizine çıkar:

`unzip -j {{yol/arşiv}}.zip {{yol/arşivdeki_dosya1 yol/arşivdeki_dosya2 ...}}`

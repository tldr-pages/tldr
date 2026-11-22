# zip

> Dosyaları paketle ve bir Zip arşivine sıkıştır (arşivle).
> Ayrıca bakınız: `unzip`.
> Daha fazla bilgi için: <https://manned.org/zip>.

- Dosyaları/dizinleri belirli bir arşive ekle:

`zip {{[-r|--recurse-paths]}} {{yol/sıkıştırılmış.zip}} {{yol/dosya_veya_dizin1 yol/dosya_veya_dizin2 ...}}`

- Dosyaları/dizinleri belirli bir arşivden kaldır:

`zip {{[-d|--delete]}} {{yol/sıkıştırılmış.zip}} {{yol/dosya_veya_dizin1 yol/dosya_veya_dizin2 ...}}`

- Belirtilenler hariç dosyaları/dizinleri arşivle:

`zip {{[-r|--recurse-paths]}} {{yol/sıkıştırılmış.zip}} {{yol/dosya_veya_dizin1 yol/dosya_veya_dizin2 ...}} {{[-x|--exclude]}} {{yol/hariç_tutulan_dosyalar_veya_dizinler}}`

- Dosyaları/dizinleri belirli bir sıkıştırma düzeyiyle arşivle (`0` - en düşük, `9` - en yüksek):

`zip {{[-r|--recurse-paths]}} -{{0..9}} {{yol/sıkıştırılmış.zip}} {{yol/dosya_veya_dizin1 yol/dosya_veya_dizin2 ...}}`

- Belirli bir parolayla şifrelenmiş bir arşiv oluştur:

`zip {{[-re|--recurse-paths --encrypt]}} {{yol/sıkıştırılmış.zip}} {{yol/dosya_veya_dizin1 yol/dosya_veya_dizin2 ...}}`

- Dosyaları/dizinleri çok parçalı bölünmüş bir Zip arşivine arşivle (örn. 3 GB'lık parçalar):

`zip {{[-rs|--recurse-paths --split-size]}} {{3g}} {{yol/sıkıştırılmış.zip}} {{yol/dosya_veya_dizin1 yol/dosya_veya_dizin2 ...}}`

- Belirli bir arşivin içeriğini yazdır:

`zip {{[-sf|--show-files]}} {{yol/sıkıştırılmış.zip}}`

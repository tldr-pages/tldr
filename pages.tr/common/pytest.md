# pytest

> Python testlerini çalıştır.
> Daha fazla bilgi için: <https://docs.pytest.org/en/latest/how-to/usage.html>.

- Belirli dosyalardaki testleri çalıştır:

`pytest {{yol/test_dosyasi1.py yol/test_dosyasi2.py ...}}`

- Adları belirli bir anahtar kelime ifadesiyle eşleşen testleri çalıştır:

`pytest -k {{ifade}}`

- Bir test başarısız olur olmaz veya hata oluştuğunda çık:

`pytest {{[-x|--exitfirst]}}`

- Belirli işaretçilerle eşleşen veya bunları hariç tutan testleri çalıştır:

`pytest -m {{isaretci1 and not isaretci2}}`

- Bir test başarısız olana kadar çalıştır, sonraki çalıştırmada son başarısız testten devam et:

`pytest {{[--sw|--stepwise]}}`

- Çıktıyı yakalamadan testleri çalıştır:

`pytest {{[-s|--capture=no]}}`

- Ayrıntı düzeyini artırarak her testin adını görüntüle:

`pytest {{[-v|--verbose]}}`

# cmake

> Çok platformlu yapım otomasyon sistemi, yerel yapım sistemleri için tarifler oluşturur.
> Daha fazla bilgi için: <https://cmake.org/cmake/help/latest/manual/cmake.1.html>.

- Bir proje dizinindeki `CMakeLists.txt` dosyasından, geçerli dizinde bir yapım tarifi oluştur:

`cmake {{proje/dizininin/yolu}}`

- Belirtilen dizinde oluşturulmuş bir tarifi kullanarak yapım çıktılarını derle:

`cmake --build {{yapım/dizininin/yolu}}`

- Yapım çıktılarını `/usr/local/` dizinine kur ve hata ayıklama sembollerini temizle:

`cmake --install {{yapım/dizininin/yolu}} --strip`

- Yapım türü CMake değişkeniyle `Release` olarak ayarlanmış bir yapım tarifi oluştur:

`cmake {{proje/dizininin/yolu}} -D CMAKE_BUILD_TYPE=Release`

- Altta yatan yapım sistemi olarak `oluşturucu_adı` kullanan bir yapım tarifi oluştur:

`cmake -G {{oluşturucu_adı}} {{proje/dizininin/yolu}}`

- Yapım çıktılarını özel bir yol öneki kullanarak kur:

`cmake --install {{yapım/dizininin/yolu}} --strip --prefix {{dizin/yolu}}`

- Özel bir yapım hedefi çalıştır:

`cmake --build {{yapım/dizininin/yolu}} {{[-t|--target]}} {{hedef_adı}}`

- Yardımı görüntüle:

`cmake {{[-h|--help]}}`

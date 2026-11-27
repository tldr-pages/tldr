# atool

> Çeşitli türlerdeki dosya arşivlerini yöneten bir betik.
> `atool`, harici arşivleme programlarını kullanır ancak arşivleri listelemek, çıkartmak, oluşturmak ve yönetmek için tutarlı bir komut satırı arayüzü sunar.
> Daha fazla bilgi için: <https://manned.org/atool>.

- Bir arşivdeki dosyaları listele:

`atool {{[-l|--list]}} {{arşiv/dosyasının/yolu.zip}}`

- Bir arşivi çıkart (gerekirse güvenli bir şekilde alt dizin oluşturur):

`atool {{[-x|--extract]}} {{arşiv.tar.gz}}`

- Bir arşivi belirli bir dizine çıkart:

`atool {{[-X|--extract-to]}} {{çıktı/dizininin/yolu}} {{arşiv.rar}}`

- Bir arşivdeki belirli bir dosyanın içeriğini `stdout`'a yazdır (`cat` gibi):

`atool {{[-c|--cat]}} {{arşiv.tar}} {{arşivdeki/dosyanın/yolu.txt}}`

- Belirtilen dosya ve/veya dizinlerden yeni bir arşiv oluştur:

`atool {{[-a|--add]}} {{yeni_arşiv.zip}} {{yol/dosya1 yol/dosya2 ...}}`

- Bir arşivdeki dosyaları listele ve çıktıyı bir sayfalayıcıdan geçir:

`atool {{[-l|--list]}} {{[-p|--page]}} {{büyük_arşiv.tar.bz2}}`

- Birden fazla arşivi aynı anda çıkart (gerekirse her birini kendi alt dizinine):

`atool {{[-x|--extract]}} {{[-e|--each]}} {{arşiv1.zip}} {{arşiv2.tar.gz}} {{*.rar}}`

- Bir arşivi bir biçimden başka bir biçime yeniden paketle (örneğin `.tar.gz` biçiminden `.tar.7z` biçimine):

`atool {{[-r|--repack]}} {{eski_arşiv.tar.gz}} {{yeni_arşiv.tar.7z}}`

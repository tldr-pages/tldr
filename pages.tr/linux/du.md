# du

> Disk kullanımını spesifik şekilde görüntülemeyi sağlayan araç.  
> Daha fazla bilgi için: <https://manned.org/du>.

- Geçerli dizindeki her dosya ve klasörün kapladığı disk alanını listele:  

`du`

- Daha anlaşılır boyut gösterimi (MB, GB vb.):  

`du -h`

- Daha anlaşılır boyut gösterimi, boyutlar 1024 değil 1000 üzerinden hesaplanır:

`du --si`

- Geçerli dizinin toplam disk kullanımını tek satırda yazdır:  

`du {{[-s|-sh|--summarize]}}`

- Geçerli dizinde sadece istenilen seviyeye kadar dizinlerin boyutunu gösterir:  

`du {{[-d|--max-depth]}}={{yazdırılacak_dizin_seviyesi}}`

- Belirtilen dizindeki tüm dosya ve alt dizinlerin boyutlarını insan okunabilir formatta gösterir:  

`du -ah {{dizin}}`

- Disk kullanımını hesaplayıp, çıktı sonunda toplam boyutu gösterir:  

`du {{[-ch|--total]}} {{dizin}}`

- Belirli dosya veya dizinleri dışlamak için:  

`du --exclude={{desen}}`

- Verilen dizgiyi içeren dosyaları hariç tut:

`du {{[-X|--exlude-from={{dizgi}}]}}`

- Dizindeki veyahut alt dizindeki dosyaların son değiştirilme tarihlerini göster:

`du --time`

- Hiçbir sembolik bağı izleme (örn. `ln` ile oluşturulan):

`du {{[-P|--no-deference]}}`

- Farklı dosya sistemlerine geçiş yapmadan aynı dosya sistemi içindeki dosya ve dizinlerin boyutlarını gösterir:  

`du {{[-xh|--one-file-system]}} {{dizin}}`

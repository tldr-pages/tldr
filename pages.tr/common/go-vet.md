# go vet

> Go kaynak kodunu kontrol et ve şüpheli yapıları bildir (örneğin Go kaynak dosyalarını tiftik et).
> Go vet komutu eğer sorun bulunduysa sıfır olmayan bir çıkış kodu yazdırır. Eğer herhangi bir sorun bulunmadıysa sıfır çıkış kodu yazdırılır.
> More information: <https://pkg.go.dev/cmd/vet>.

- Mevcut dizindeki Go paketini kontrol et:

`go vet`

- Belirtilen yoldaki Go paketini kontrol et:

`go vet {{örnek/dosya_veya_dizin}}`

- Go vet ile çalıştırılabilecek erişilebilir kontrolleri sırala:

`go tool vet help`

- Belirtilen bir kontrol için detayları ve bayrakları göster:

`go tool vet help {{kontrol_ismi}}`

- Kontrolün sorun bulmasına sebep olan satırları artı N sayıda ek içeriği görüntüle:

`go vet -c={{N}}`

- Analiz ve hataları JSON formatında çıkart:

`go vet -json`

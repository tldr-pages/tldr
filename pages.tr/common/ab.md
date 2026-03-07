# ab

> Apache HTTP sunucusu kıyaslama aracı.
> Daha fazla bilgi için: <https://httpd.apache.org/docs/current/programs/ab.html>.

- Belirli bir URL'ye 100 HTTP GET isteği gönder:

`ab -n 100 {{url}}`

- Bir URL'ye, 10'luk eşzamanlı partiler halinde 100 HTTP GET isteği gönder:

`ab -n 100 -c 10 {{url}}`

- Bir dosyadan JSON verisi kullanarak bir URL'ye 100 HTTP POST isteği gönder:

`ab -n 100 -T {{application/json}} -p {{yol/dosya.json}} {{url}}`

- HTTP [k]eep-Alive kullan, yani tek bir HTTP oturumu içinde birden fazla istek gerçekleştir:

`ab -k {{url}}`

- Kıyaslama için harcanacak maksimum süreyi ([t]imeout) saniye cinsinden ayarla (varsayılan 30):

`ab -t {{60}} {{url}}`

- Sonuçları bir CSV dosyasına yaz:

`ab -e {{yol/dosya.csv}}`

# nodemon

> Dosyalar değiştirildiğinde Node uygulamasını yeniden başlatmak için dosyaları izler.
> Daha fazla bilgi için: <https://github.com/remy/nodemon/tree/main/doc/cli>.

- Verilen dosyayı çalıştırır ve belirtilen dosyadaki değişiklikleri izler:

`nodemon {{dosya/yolu/dosya.js}}`

- Nodemon'u el ile yeniden başlatır (not: bu işlem için nodemon zaten aktif olmalıdır):

`rs`

- Belirli dosyaları göz ardı eder:

`nodemon --ignore {{dosya/yolu/dosya_veya_dizin}}`

- Node uygulamasına argümanlar geçirir:

`nodemon {{dosya/yolu/dosya.js}} {{argümanlar}}`

- Zaten Nodemon argümanları değillerse argümanları Node'un kendisine geçirir (örneğin: `--inspect`):

`nodemon {{argümanlar}} {{dosya/yolu/dosya.js}}`

- Node olmayan bir komut dosyasını çalıştırır:

`nodemon --exec "{{komut}} {{seçenekler}}" {{dosya/yolu/komut}}`

- Python kodunu çalıştırır:

`nodemon --exec "python {{seçenekler}}" {{dosya/yolu/dosya.py}}`

# nodemon

> Dosyalar değiştirildiğinde Node uygulamasını yeniden başlatmak için dosyaları izler.
> Daha fazla bilgi: <https://nodemon.io>.

- Verilen dosyayı çalıştırır ve belirtilen dosyadaki değişiklikleri izler:

`nodemon {{path/to/file.js}}`

- Nodemon'u el ile yeniden başlatır (not: bu işlem için nodemon zaten aktif olmalıdır):

`rs`

- Belirli dosyaları göz ardı eder:

`nodemon --ignore {{path/to/file_or_directory}}`

- Node uygulamasına argümanlar geçirir:

`nodemon {{path/to/file.js}} {{arguments}}`

- Zaten Nodemon argümanları değillerse argümanları Node'un kendisine geçirir (örneğin: `--inspect`):

`nodemon {{arguments}} {{path/to/file.js}}`

- Node olmayan bir komut dosyasını çalıştırır:

`nodemon --exec "{{command_to_run_script}} {{options}}" {{path/to/script}}`

- Python kodunu çalıştırır:

`nodemon --exec "python {{options}}" {{path/to/file.py}}`

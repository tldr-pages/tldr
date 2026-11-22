# python

> Python dili yorumlayıcısı.
> Daha fazla bilgi için: <https://docs.python.org/using/cmdline.html>.

- Bir REPL (etkileşimli kabuk) başlat:

`python`

- Belirli bir Python dosyasını çalıştır:

`python {{yol/dosya.py}}`

- Belirli bir Python dosyasını çalıştır ve bir REPL başlat:

`python -i {{yol/dosya.py}}`

- Bir Python ifadesini çalıştır:

`python -c "{{ifade}}"`

- Belirtilen kütüphane modülünün betiğini çalıştır:

`python -m {{modül}} {{argümanlar}}`

- `pip` kullanarak bir paket kur:

`python -m pip install {{paket}}`

- Bir Python betiğinde etkileşimli olarak hata ayıkla:

`python -m pdb {{yol/dosya.py}}`

- Yerleşik HTTP sunucusunu geçerli dizinde 8000 portunda başlat:

`python -m http.server`

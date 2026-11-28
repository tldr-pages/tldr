# pip

> Python paket yöneticisi.
> `install` gibi bazı alt komutların kendi kullanım dokümantasyonu vardır.
> Daha fazla bilgi için: <https://pip.pypa.io/en/stable/cli/pip/>.

- Bir paket kur (daha fazla kurulum örneği için `pip install` sayfasına bak):

`pip install {{paket}}`

- Bir paketi sistem genelindeki varsayılan konum yerine kullanıcının dizinine kur:

`pip install --user {{paket}}`

- Bir paketi yükselt:

`pip install {{[-U|--upgrade]}} {{paket}}`

- Bir paketi kaldır:

`pip uninstall {{paket}}`

- Kurulu paketleri bir dosyaya kaydet:

`pip freeze >{{requirements.txt}}`

- Kurulu paketleri listele:

`pip list`

- Kurulu bir paketin bilgilerini göster:

`pip show {{paket}}`

- Paketleri bir dosyadan kur:

`pip install {{[-r|--requirement]}} {{requirements.txt}}`

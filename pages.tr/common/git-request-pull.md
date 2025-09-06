# git request-pull

> Ana projeye yerelde yapılan değişiklikleri kendi ağacına çekmesini sormak için izin hazırla.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-request-pull>.

- v1.1 sürümü ve belirtilen dal arasındaki değişiklikleri özetleyen bir izin üret:

`git request-pull {{v1.1}} {{https://ornek.com/proje}} {{dal_ismi}}`

- `foo` dalındaki v0.1 sürümü ile yereldeki `bar` dalları arasındaki değişiklikleri özetleyen bir izin üret:

`git request-pull {{v0.1}} {{https://ornek.com/proje}} {{foo:bar}}`

# git check-ignore

> Git yoksayma / dışlama (".gitignore") dosyalarını analiz et.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-check-ignore>.

- Bir dosya veya dizinin yoksayıldığı veya sayılmadığını kontrol et:

`git check-ignore {{örnek/dosya_veya_dizin}}`

- Birden fazla dosya veya dizinin yoksayıldığı veya sayılmadığını kontrol et:

`git check-ignore {{örnek/dosya_veya_dizin1 örnek/dosya_veya_dizin2 ...}}`

- Her bir satıra tekabül edecek şekilde `stdin`'den yolisimleri kullan:

`git check-ignore --stdin < {{örnek/dosya_sırası}}`

- İndeksi kontrol etme:

`git check-ignore --no-index {{örnek/dosya_veya_dizin1 örnek/dosya_veya_dizin2 ...}}`

- Her yol için eşleşen desene dair detayları dahil et:

`git check-ignore --verbose {{örnek/dosya_veya_dizin1 örnek/dosya_veya_dizin2 ...}}`

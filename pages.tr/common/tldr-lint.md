# tldr-lint

> `tldr` sayfalarını gözden geçir ve biçimlendir.
> Not: `tldrl`, `tldr-lint` için takma ad olarak kullanılabilir.
> Daha fazla bilgi için: <https://github.com/tldr-pages/tldr-lint#usage>.

- Tek bir sayfayı ya da bir dizindeki tüm sayfaları gözden geçir:

`tldr-lint {{yol/sayfa_veya_dizin}}`

- Gözden geçirirken belirli `tldr-lint` hata kodlarını yok say:

`tldr-lint {{[-I|--ignore]}} {{TLDR001,TLDR002,...}} {{yol/sayfa_veya_dizin}}`

- Belirli bir sayfayı `stdout`'a biçimlendir:

`tldr-lint {{[-f|--format]}} {{yol/sayfa.md}}`

- Bir sayfayı yerinde biçimlendir:

`tldr-lint {{[-f|--format]}} {{[-i|--in-place]}} {{yol/sayfa.md}}`

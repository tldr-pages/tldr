# կախարդական նույնականացում

> Նկարագրեք պատկերային ֆայլերի ձևաչափը և բնութագրերը:.
> Տես նաև՝ `magick`:.
> Լրացուցիչ տեղեկություններ. <https://imagemagick.org/script/identify.php>:.

- Նկարագրեք պատկերի ձևաչափը և հիմնական բնութագրերը.:

`magick identify {{path/to/image}}`

- Նկարագրեք պատկերի ձևաչափը և մանրամասն բնութագրերը.:

`magick identify -verbose {{path/to/image}}`

- Հավաքեք բոլոր JPEG ֆայլերի չափերը ընթացիկ գրացուցակում և պահեք դրանք CSV ֆայլում.:

`magick identify -format "{{%f,%w,%h\n}}" {{*.jpg}} > {{path/to/filelist.csv}}`

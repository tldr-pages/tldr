# cdparanoia

> Հեռացրեք ձայնային հետքերը CD-ներից:.
> Լրացուցիչ տեղեկություններ. <https://xiph.org/paranoia/manual.html>:.

- Քաղեք բոլոր հետքերը և գրեք դրանք առանձին WAV ֆայլերում՝ `track#.wav` անունով:

`cdparanoia {{[-B|--batch]}}`

- Տպեք CD-ի բովանդակության աղյուսակը տերմինալում.:

`cdparanoia {{[-Q|--query]}}`

- Քաղեք 2-ից 5-րդ հետքերը և գրեք դրանք մեկ WAV ֆայլի մեջ.:

`cdparanoia 2-5`

- Քաղեք 3-րդ կատարումը և գրեք այն ֆայլում, որը կոչվում է `path/to/file.wav`:

`cdparanoia 3 '{{path/to/file.wav}}'`

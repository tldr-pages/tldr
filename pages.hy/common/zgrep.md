# zgrep

> Գրեք տեքստի նախշերը սեղմված ֆայլերի մեջ գտնվող ֆայլերից:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/zgrep>:.

- Գրեք օրինաչափություն սեղմված ֆայլում (գործի զգայուն).:

`zgrep {{pattern}} {{path/to/compressed_file}}`

- Տպեք [C] տեքստի 3 տող շուրջը, [B]նախօրոք կամ [A]յուրաքանչյուր համընկնումից հետո.:

`zgrep {{--context|--before-context|--after-context}} 3 {{pattern}} {{path/to/compressed_file}}`

- Գրեք օրինաչափություն սեղմված ֆայլում (տառերի նկատմամբ զգայուն).:

`zgrep {{[-i|--ignore-case]}} {{pattern}} {{path/to/compressed_file}}`

- Սեղմված ֆայլում համընկնող օրինակ պարունակող տողերի ելքային քանակը.:

`zgrep {{[-c|--count]}} {{pattern}} {{path/to/compressed_file}}`

- Ցուցադրել այն տողերը, որոնք չունեն նախշը (շրջել որոնման գործառույթը).:

`zgrep {{[-v|--invert-match]}} {{pattern}} {{path/to/compressed_file}}`

- Գրեք սեղմված ֆայլ բազմաթիվ նախշերի համար.:

`zgrep {{[-e|--regexp]}} "{{pattern_1}}" {{[-e|--regexp]}} "{{pattern_2}}" {{path/to/compressed_file}}`

- Օգտագործեք ընդլայնված `regex` (աջակցում է `?`, `+`, `{}`, `()` և `|`):

`zgrep {{[-E|--extended-regexp]}} {{regex}} {{path/to/file}}`

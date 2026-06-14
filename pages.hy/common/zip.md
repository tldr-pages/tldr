# zip

> Փաթեթավորեք և սեղմեք (արխիվային) ֆայլերը Zip արխիվի մեջ:.
> Տես նաև՝ `unzip`:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/zip>:.

- Ավելացնել ֆայլեր/տեղեկատուներ հատուկ արխիվում.:

`zip {{[-r|--recurse-paths]}} {{path/to/compressed.zip}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Հեռացրեք ֆայլերը / գրացուցակները հատուկ արխիվից.:

`zip {{[-d|--delete]}} {{path/to/compressed.zip}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Արխիվային ֆայլեր/տեղեկատուներ, բացառությամբ նշվածների.:

`zip {{[-r|--recurse-paths]}} {{path/to/compressed.zip}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}} {{[-x|--exclude]}} {{path/to/excluded_files_or_directories}}`

- Արխիվացրեք ֆայլերը/գրացուցակները հատուկ սեղմման մակարդակով (`0` - ամենացածրը, `9` - ամենաբարձրը).:

`zip {{[-r|--recurse-paths]}} -{{0..9}} {{path/to/compressed.zip}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Ստեղծեք կոդավորված արխիվ հատուկ գաղտնաբառով.:

`zip {{[-re|--recurse-paths --encrypt]}} {{path/to/compressed.zip}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Արխիվացրեք ֆայլերը/տեղեկատուները մի քանի մասից բաժանված Zip արխիվում (օրինակ՝ 3 ԳԲ մասեր).:

`zip {{[-rs|--recurse-paths --split-size]}} {{3g}} {{path/to/compressed.zip}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Տպել հատուկ արխիվի բովանդակություն.:

`zip {{[-sf|--split-size --freshen]}} {{path/to/compressed.zip}}`

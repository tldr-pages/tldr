#մմ

> Հեռացրեք ֆայլերը կամ գրացուցակները:.
> Տես նաև՝ `rmdir`, `trash`:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/coreutils/manual/html_node/rm-invocation.html>:.

- Հեռացրեք հատուկ ֆայլեր.:

`rm {{path/to/file1 path/to/file2 ...}}`

- Հեռացրեք հատուկ ֆայլեր՝ անտեսելով գոյություն չունեցողները.:

`rm {{[-f|--force]}} {{path/to/file1 path/to/file2 ...}}`

- Հեռացրեք հատուկ ֆայլեր, որոնք ինտերակտիվ կերպով հուշում են յուրաքանչյուր հեռացումից առաջ.:

`rm {{[-i|--interactive]}} {{path/to/file1 path/to/file2 ...}}`

- Հեռացրեք յուրաքանչյուր հեռացման մասին հատուկ ֆայլերի տպագրության տեղեկությունները.:

`rm {{[-v|--verbose]}} {{path/to/file1 path/to/file2 ...}}`

- Հեռացրեք որոշակի ֆայլեր և գրացուցակներ ռեկուրսիվ կերպով.:

`rm {{[-r|--recursive]}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Հեռացրեք դատարկ գրացուցակները (սա համարվում է անվտանգ մեթոդ).:

`rm {{[-d|--dir]}} {{path/to/directory}}`

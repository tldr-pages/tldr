# վեբփոթորիկ

> JetBrains JavaScript IDE:.
> Լրացուցիչ տեղեկություններ. <https://www.jetbrains.com/help/webstorm/working-with-the-ide-features-from-command-line.html>:.

- Բացեք ընթացիկ գրացուցակը WebStorm-ում.:

`webstorm`

- Բացեք հատուկ գրացուցակ WebStorm-ում.:

`webstorm {{path/to/directory}}`

- Բացեք հատուկ ֆայլեր LightEdit ռեժիմում.:

`webstorm -e {{path/to/file1 path/to/file2 ...}}`

- Բացեք և սպասեք, մինչև ավարտվի որոշակի ֆայլի խմբագրումը LightEdit ռեժիմում.:

`webstorm --wait -e {{path/to/file}}`

- Բացեք ֆայլը կուրսորով կոնկրետ տողում.:

`webstorm --line {{line_number}} {{path/to/file}}`

- Բացեք և համեմատեք ֆայլերը (աջակցում է մինչև 3 ֆայլ).:

`webstorm diff {{path/to/file1 path/to/file2 path/to/optional_file3}}`

- Բացեք և կատարեք եռակողմ միաձուլում.:

`webstorm merge {{path/to/left_file}} {{path/to/right_file}} {{path/to/target_file}}`

# փոցխ

> Ռուբիի համար նախատեսված ծրագիր:.
> `rake`-ի առաջադրանքները նշված են Rakefile-ում:.
> Լրացուցիչ տեղեկություններ. <https://ruby.github.io/rake/>:.

- Գործարկեք `default` Rakefile առաջադրանքը՝:

`rake`

- Գործարկել կոնկրետ առաջադրանք.:

`rake {{task}}`

- Զուգահեռաբար կատարեք `n` աշխատանքներ (CPU միջուկների թիվը + 4 ըստ լռելյայն).:

`rake --jobs {{n}}`

- Օգտագործեք հատուկ Rakefile:

`rake --rakefile {{path/to/Rakefile}}`

- Կատարեք `rake` մեկ այլ գրացուցակից.:

`rake --directory {{path/to/directory}}`

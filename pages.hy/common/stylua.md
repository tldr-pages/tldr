# ստիլուա

> Համոզված Lua կոդերի ձևաչափիչ:.
> Լրացուցիչ տեղեկություններ. <https://github.com/JohnnyMorganz/StyLua>:.

- Ֆայլի կամ ամբողջ գրացուցակի ավտոմատ ձևաչափում.:

`stylua {{path/to/file_or_directory}}`

- Ստուգեք, արդյոք որոշակի ֆայլ ֆորմատավորված է.:

`stylua --check {{path/to/file}}`

- Գործարկել հատուկ կազմաձևման ֆայլով.:

`stylua --config-path {{path/to/config_file}} {{path/to/file}}`

- Ձևաչափեք կոդը `stdin`-ից և թողարկեք `stdout`:

`stylua - < {{path/to/file.lua}}`

- Ձևաչափեք ֆայլը կամ գրացուցակը՝ օգտագործելով բացատները և նախընտրելով միայնակ չակերտները.:

`stylua --indent-type {{Spaces}} --quote-style {{AutoPreferSingle}} {{path/to/file_or_directory}}`

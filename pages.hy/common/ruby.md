#ռուբին

> Ruby ծրագրավորման լեզվի թարգմանիչ:.
> Տես նաև՝ `gem`, `bundler`, `rake`, `irb`, `ri`:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/ruby>:.

- Կատարել Ruby սցենար.:

`ruby {{path/to/script.rb}}`

- Կատարեք մեկ Ruby հրաման հրամանի տողում.:

`ruby -e "{{command}}"`

- Ստուգեք տրված Ruby սկրիպտի շարահյուսական սխալների համար.:

`ruby -c {{path/to/script.rb}}`

- Գործարկեք ներկառուցված HTTP սերվերը 8080 նավահանգստում ընթացիկ գրացուցակում.:

`ruby -run -e httpd`

- Տեղականորեն կատարեք Ruby երկուական տարբերակ՝ առանց անհրաժեշտ գրադարանը տեղադրելու, դա կախված է.:

`ruby -I {{path/to/library_folder}} -r {{library_require_name}} {{path/to/bin_folder/bin_name}}`

- Ցուցադրման տարբերակը:

`ruby {{[-v|--version]}}`

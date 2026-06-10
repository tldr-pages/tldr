#մինչև

> Պարզ կեղևի հանգույց, որը կրկնվում է այնքան ժամանակ, մինչև այն ստանա զրո որպես վերադարձի արժեք:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/bash/manual/bash.html#index-until>:.

- Կատարեք հրաման, մինչև այն հաջողվի.:

`until {{command}}; do :; done`

- Փորձեք միանալ SSH հոսթին մինչև նրբորեն անջատվելը.:

`until ssh {{username}}@{{host}}; do sleep {{2}}; done`

- Սպասեք, մինչև համակարգային ծառայությունն ակտիվանա.:

`until systemctl is-active {{[-q|--quiet]}} {{nginx}}; do {{echo "Waiting..."}}; sleep 1; done; {{echo "Launched!"}}`

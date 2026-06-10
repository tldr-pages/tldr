# fx

> Դիտեք և մշակեք JSON-ը:.
> Լրացուցիչ տեղեկություններ. <https://fx.wtf/getting-started>:.

- Դիտեք JSON ֆայլը ինտերակտիվ կերպով.:

`fx {{path/to/file.json}}`

- Գեղեցիկ տպեք և գունավորեք JSON-ը `stdin`-ից:

`cat {{path/to/file.json}} | fx`

- Բացեք JSON տվյալները URL-ից.:

`curl {{url}} | fx`

- Զտել JSON-ը՝ օգտագործելով JavaScript-ի նման արտահայտություններ.:

`fx {{path/to/file.json}} {{.name}}`

- Վերլուծեք TOML մուտքագրված ֆայլը JSON-ում.:

`fx --toml {{path/to/file.toml}}`

- Վերլուծեք YAML մուտքագրված ֆայլը JSON-ում.:

`fx --yaml {{path/to/file.yaml}}`

# էջ

> Լուսանկարեք կայքերի սքրինշոթներ տարբեր լուծումներով:.
> Լրացուցիչ տեղեկություններ. <https://github.com/sindresorhus/pageres-cli>:.

- Վերցրեք բազմաթիվ URL-ների բազմաթիվ սքրինշոթներ տարբեր լուծումներով.:

`pageres {{https://example.com/}} {{https://example2.com/}} {{1366x768}} {{1600x900}}`

- Տրամադրեք հատուկ ընտրանքներ URL-ի համար՝ գերակայող գլոբալ տարբերակները.:

`pageres [{{https://example.com/}} {{1366x768}} --no-crop] [{{https://example2.com/}} {{1024x768}}] {{[-c|--crop]}}`

- Տրամադրել հատուկ ֆայլի անվան ձևանմուշ.:

`pageres {{https://example.com/}} {{1024x768}} --filename='{{<%= date %> - <%= url %>}}'`

- Գրեք որոշակի տարր էջի վրա.:

`pageres {{https://example.com/}} {{1366x768}} --selector='{{.page-header}}'`

- Թաքցնել որոշակի տարր.:

`pageres {{https://example.com/}} {{1366x768}} --hide='{{.page-header}}'`

- Լուսանկարեք տեղական ֆայլի սքրինշոթ.:

`pageres {{path/to/local_file.html}} {{1366x768}}`

#փարոս

> Վերլուծում է վեբ հավելվածները և վեբ էջերը՝ հավաքելով կատարողականի ժամանակակից ցուցանիշներ և պատկերացումներ մշակողների լավագույն փորձի վերաբերյալ:.
> Լրացուցիչ տեղեկություններ. <https://github.com/GoogleChrome/lighthouse#cli-options>:.

- Ստեղծեք HTML հաշվետվություն կոնկրետ կայքի համար և պահեք այն ընթացիկ գրացուցակի ֆայլում.:

`lighthouse {{https://example.com}}`

- Ստեղծեք JSON զեկույց և տպեք այն.:

`lighthouse --output {{json}} {{https://example.com}}`

- Ստեղծեք JSON զեկույց և պահեք այն որոշակի ֆայլում.:

`lighthouse --output {{json}} --output-path {{path/to/file.json}} {{https://example.com}}`

- Ստեղծեք զեկույց՝ օգտագործելով զննարկիչը առանց գլխի ռեժիմում՝ առանց մուտք գործելու `stdout`:

`lighthouse --quiet --chrome-flags="{{--headless}}" {{https://example.com}}`

- Ստեղծեք հաշվետվություն՝ օգտագործելով HTTP վերնագրի ստեղնի/արժեքի զույգերը նշված JSON ֆայլում բոլոր հարցումների համար.:

`lighthouse --extra-headers={{path/to/file.json}} {{https://example.com}}`

- Ստեղծեք հաշվետվություն միայն հատուկ կատեգորիաների համար.:

`lighthouse --only-categories={{performance,accessibility,best-practices,seo,pwa}} {{https://example.com}}`

- Ստեղծեք հաշվետվություն սարքի էմուլյացիայով և բոլոր throttling անջատված.:

`lighthouse --screenEmulation.disabled --throttling-method={{provided}} --no-emulatedUserAgent {{https://example.com}}`

- Ցուցադրել օգնությունը.:

`lighthouse --help`

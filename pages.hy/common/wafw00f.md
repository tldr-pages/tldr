# wafw00f

> Բացահայտեք և մատնահետքերով հայտնաբերեք Web Application Firewall (WAF) արտադրանքները, որոնք պաշտպանում են կայքը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/EnableSecurity/wafw00f/wiki/Usage#arguments-list>:.

- Ստուգեք, արդյոք վեբկայքն օգտագործում է որևէ WAF:

`wafw00f {{https://www.example.com}}`

- Փորձարկեք բոլոր հայտնաբերվող WAF-ների համար՝ առանց կանգ առնելու առաջին հանդիպման ժամանակ.:

`wafw00f {{[-a|--findall]}} {{https://www.example.com}}`

- Անցեք հարցումները վստահված անձի միջոցով (օրինակ՝ BurpSuite).:

`wafw00f {{[-p|--proxy]}} {{http://localhost:8080}} {{https://www.example.com}}`

- Փորձարկեք կոնկրետ WAF արտադրանքի համար (գործարկեք `wafw00f --list`՝ բոլոր աջակցվող WAF-ների ցանկը ստանալու համար).:

`wafw00f {{[-t|--test]}} {{Cloudflare|Cloudfront|Fastly|ZScaler|...}} {{https://www.example.com}}`

- Անցեք հատուկ վերնագրեր ֆայլից.:

`wafw00f {{[-H|--headers]}} {{path/to/headers.txt}} {{https://www.example.com}}`

- Կարդացեք թիրախային մուտքերը ֆայլից և ցուցադրեք բովանդակալից ելք (բազմաթիվ `v` ավելի շատ պարզաբանության համար).:

`wafw00f {{[-i|--input]}} {{path/to/urls.txt}} -{{vv}}`

- Թվարկեք բոլոր WAF-ները, որոնք կարող են հայտնաբերվել.:

`wafw00f {{[-l|--list]}}`

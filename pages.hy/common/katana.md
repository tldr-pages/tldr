#կատանա

> Արագ սողուն, որը կենտրոնացած է ավտոմատացման խողովակաշարերում կատարման վրա, որն առաջարկում է ինչպես անգլուխ, այնպես էլ անգլուխ սողալ:.
> Տես նաև՝ `gau`, `scrapy`, `waymore`:.
> Լրացուցիչ տեղեկություններ. <https://docs.projectdiscovery.io/opensource/katana/usage>:.

- Ուղարկեք URL-ների ցանկը՝:

`katana -list {{https://example.com,https://google.com,...}}`

- Սխալեք [u]RL՝ առանց գլխի ռեժիմի՝ Chromium-ի միջոցով.:

`katana -u {{https://example.com}} {{[-hl|-headless]}}`

- Անցեք հարցումները վստահված անձի միջոցով (http/socks5) և օգտագործեք հատուկ վերնագրեր ֆայլից.:

`katana -proxy {{http://127.0.0.1:8080}} {{[-H|-headers]}} {{path/to/headers.txt}} -u {{https://example.com}}`

- Նշեք սողալու ռազմավարությունը, ենթագրքերների խորությունը, որով կարող եք սողալ և արագության սահմանափակում (հարցումներ վայրկյանում).:

`katana {{[-s|-strategy]}} {{depth-first|breadth-first}} {{[-d|-depth]}} {{value}} {{[-rl|-rate-limit]}} {{value}} -u {{https://example.com}}`

- Գտեք ենթադոմեյններ՝ օգտագործելով `subfinder`, յուրաքանչյուրը սողալ առավելագույն թվով վայրկյանների ընթացքում և արդյունքները գրեք ելքային ֆայլում՝:

`subfinder {{[-dL|-list]}} {{path/to/domains.txt}} | katana {{[-ct|-crawl-duration]}} {{value}} {{[-o|-output]}} {{path/to/output.txt}}`

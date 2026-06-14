#մորեխ

> Բեռնվածության փորձարկման գործիք՝ որոշելու միաժամանակյա օգտագործողների թիվը, որոնց համակարգը կարող է գործածել:.
> Լրացուցիչ տեղեկություններ. <https://docs.locust.io/en/stable/configuration.html#configuration>:.

- Load-test «example.com» վեբ ինտերֆեյսի միջոցով՝ օգտագործելով locustfile.py:

`locust {{[-H|--host]}} {{http://example.com}}`

- Օգտագործեք մեկ այլ թեստային ֆայլ.:

`locust {{[-H|--host]}} {{http://example.com}} {{[-f|--locustfile]}} {{test_file.py}}`

- Գործարկեք թեստը առանց վեբ ինտերֆեյսի՝ վայրկյանում 1 օգտատեր առաջացնելով մինչև 100 օգտվող լինի.:

`locust {{[-H|--host]}} {{http://example.com}} --headless {{[-u|--users]}} 100 {{[-r|--spawn-rate]}} 1`

- Սկսեք Locust-ը վարպետ ռեժիմում.:

`locust {{[-H|--host]}} {{http://example.com}} --master`

- Միացրեք Locust-ի աշխատողին վարպետին.:

`locust {{[-H|--host]}} {{http://example.com}} --worker`

- Միացրեք Locust-ի աշխատողին այլ մեքենայի վրա տիրապետելու համար.:

`locust {{[-H|--host]}} {{http://example.com}} --worker --master-host {{master_hostname}}`

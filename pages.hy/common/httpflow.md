# http հոսք

> Կոմունալ ծրագիր՝ HTTP հոսքերը գրավելու և թափելու համար:.
> Լրացուցիչ տեղեկություններ. <https://github.com/six-ddc/httpflow>:.

- Գրավել երթևեկությունը բոլոր ինտերֆեյսներում.:

`httpflow -i {{any}}`

- Արդյունքները զտելու համար օգտագործեք bpf ոճի նկարահանում.:

`httpflow {{host httpbin.org or host baidu.com}}`

- Օգտագործեք `regex` հարցումները URL-ներով զտելու համար.:

`httpflow -u '{{regex}}'`

- Կարդացեք փաթեթները PCAP ձևաչափի երկուական ֆայլից.:

`httpflow -r {{out.cap}}`

- Արդյունքը գրեք գրացուցակում.:

`httpflow -w {{path/to/directory}}`

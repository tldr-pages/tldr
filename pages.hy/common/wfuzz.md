# wfuzz

> Վեբ հավելված bruteforcer:.
> Լրացուցիչ տեղեկություններ. <https://wfuzz.readthedocs.io/en/latest/user/basicusage.html>:.

- Տեղեկատու և ֆայլի bruteforce՝ օգտագործելով նշված [w]ordlist-ը և նաև [p]roxying տրաֆիկը.:

`wfuzz -w {{path/to/file}} -p {{127.0.0.1:8080:HTTP}} {{http://example.com/FUZZ}}`

- Արդյունքները պահեք [f] ֆայլում՝:

`wfuzz -w {{path/to/file}} -f {{filename}} {{http://example.com/FUZZ}}`

- Ցույց տալ [c]գունավորված ելքը՝ միայն ելքի մեջ ցույց տալով հայտարարված պատասխանի կոդերը.:

`wfuzz -c -w {{path/to/file}} --sc {{200,301,302}} {{http://example.com/FUZZ}}`

- Օգտագործեք հատուկ [H]eader՝ ենթադոմեյնները շփոթելու համար, մինչդեռ [h] թաքցնում եք կոնկրետ պատասխանների [c] կոդեր և բառերի հաշվառում: Բարձրացրեք [t] շղթաները մինչև 100 և ներառեք թիրախային IP/տիրույթը՝:

`wfuzz -w {{path/to/file}} -H "{{Host: FUZZ.example.com}}" --hc {{301}} --hw {{222}} -t {{100}} {{example.com}}`

- Կոպիտ ուժի հիմնական նույնականացում՝ օգտագործելով օգտանունների և գաղտնաբառերի ցուցակը ֆայլերից յուրաքանչյուր FUZ[z] հիմնաբառի համար, [h]իսկ անհաջող փորձերի պատասխանները.:

`wfuzz -c --hc {{401}} -s {{delay_between_requests_in_seconds}} -z file,{{path/to/usernames}} -z file,{{path/to/passwords}} --basic 'FUZZ:FUZ2Z' {{https://example.com}}`

- Տրամադրեք բառացանկ անմիջապես հրամանի տողից և օգտագործեք POST հարցումը fuzzing-ի համար.:

`wfuzz -z list,{{word1-word2-...}} {{https://api.example.com}} -d "{{id=FUZZ&showwallet=true}}"`

- Տրամադրեք բառացանկեր մի ֆայլից, որը կիրառում է base64 և md5 կոդավորումը դրանց վրա (`wfuzz -e encoders` թվարկում է բոլոր հասանելի կոդավորիչները):

`wfuzz -z file,{{path/to/file}},none-base64-md5 {{https://example.com/FUZZ}}`

- Ցուցակեք առկա կոդավորիչները/վճարվող բեռները/կրկնիչները/տպիչները/սկրիպտները.:

`wfuzz -e {{encoders|payloads|iterators|printers|scripts}}`

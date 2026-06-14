#ֆֆֆ

> Արագ վեբ fuzzer գրված Go-ում:.
> `FUZZ` հիմնաբառը օգտագործվում է որպես տեղապահ: `ffuf`-ը կփորձի հարվածել URL-ին՝ փոխարինելով `FUZZ` բառը բառացանկի յուրաքանչյուր բառով:.
> Լրացուցիչ տեղեկություններ. <https://github.com/ffuf/ffuf#usage>:.

- Թվարկեք դիրեկտորիաները՝ օգտագործելով [c]գունավոր ելքը և [w]ordlist, որը նշում է թիրախ [u]RL:

`ffuf -c -w {{path/to/wordlist.txt}} -u {{https://example.com/FUZZ}}`

- Թվարկե՛ք ենթադոմեյնների վեբսերվերները՝ փոխելով հիմնաբառի դիրքը.:

`ffuf -w {{path/to/subdomains.txt}} -u {{https://FUZZ.example.com}}`

- Fuzz նշված [t]թելերով (կանխադրված՝ 40) և pro[x]y երթևեկությունը և պահպանեք [o]ելքը ֆայլում:

`ffuf -o -w {{path/to/wordlist.txt}} -u {{https://example.com/FUZZ}} -t {{500}} -x {{http://127.0.0.1:8080}}`

- Fuzz կոնկրետ [H]eader («Name: Value») և [m]atch HTTP կարգավիճակի [c]odes:

`ffuf -w {{path/to/wordlist.txt}} -u {{https://example.com}} -H "{{Host: FUZZ}}" -mc {{200}}`

- Fuzz նշված HTTP մեթոդի և [d]ata-ի հետ՝ միաժամանակ [f]զտելով հատուկ կարգավիճակի [c] կոդերն ու պատասխանի [s] չափը.:

`ffuf -w {{path/to/postdata.txt}} -X {{POST}} -d "{{username=admin\&password=FUZZ}}" -u {{https://example.com/login.php}} -fc {{302,401-499}} -fs {{1234}}`

- Բազմաթիվ դիրքեր միացրեք բազմաթիվ բառացանկերով՝ օգտագործելով տարբեր ռեժիմներ և [a]uto [c] calibration՝ կեղծ դրականները նվազեցնելու համար.:

`ffuf -w {{path/to/keys:KEY}} -w {{path/to/values:VALUE}} -mode {{pitchfork|clusterbomb}} -u {{https://example.com/id?KEY=VALUE}} -ac`

- Վստահված անձի հարցումներ HTTP MITM pro[x]y-ի միջոցով (օրինակ՝ Burp Suite կամ `mitmproxy`):

`ffuf -w {{path/to/wordlist}} -x {{http://127.0.0.1:8080}} -u {{https://example.com/FUZZ}}`

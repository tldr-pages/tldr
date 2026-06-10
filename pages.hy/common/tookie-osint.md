# Takeie-osint

> Օգտվողի անունը OSINT սկաներ:.
> Լրացուցիչ տեղեկություններ. <https://github.com/Alfredredbird/tookie-osint>:.

- Սկանավորեք օգտվողի անունը.:

`tookie-osint {{[-u|--user]}} {{username}}`

- Սկանավորեք օգտանունը JSON ելքով և 10 թելերով.:

`tookie-osint {{[-u|--user]}} {{username}} {{[-o|--output]}} json {{[-t|--threads]}} 10`

- Սկանավորեք օգտվողի անունները CSV ելքով ֆայլից.:

`tookie-osint {{[-U|--userfile]}} {{path/to/users.txt}} {{[-o|--output]}} csv`

- Սկանավորեք օգտվողի անունը վստահված անձի միջոցով և ցույց տվեք բոլոր արդյունքները.:

`tookie-osint {{[-u|--user]}} {{username}} {{[-p|--proxy]}} {{http://127.0.0.1:8080}} {{[-a|--all]}}`

- Սկանավորեք օգտվողի անունը միացված վեբքերիչի միջոցով.:

`tookie-osint {{[-u|--user]}} {{username}} {{[-W|--webscraper]}}`

- Ցուցադրել օգնությունը.:

`tookie-osint {{[-h|--help]}}`

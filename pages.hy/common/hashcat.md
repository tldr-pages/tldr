# hashcat

> Արագ և առաջադեմ գաղտնաբառի վերականգնման գործիք:.
> Լրացուցիչ տեղեկություններ. <https://hashcat.net/wiki/doku.php?id=hashcat>:.

- Կատարեք կոպիտ ուժային հարձակում (ռեժիմ 3) կանխադրված հեշկատ դիմակով.:

`hashcat {{[-m|--hash-type]}} {{hash_type_id}} {{[-a|--attack-mode]}} 3 {{hash_value}}`

- Կատարեք բիրտ ուժի հարձակում (ռեժիմ 3) 4 նիշերի հայտնի օրինակով.:

`hashcat {{[-m|--hash-type]}} {{hash_type_id}} {{[-a|--attack-mode]}} 3 {{hash_value}} "{{?d?d?d?d}}"`

- Կատարեք կոպիտ ուժային հարձակում (ռեժիմ 3)՝ օգտագործելով բոլոր տպվող ASCII նիշերից առավելագույնը 8-ը.:

`hashcat {{[-m|--hash-type]}} {{hash_type_id}} {{[-a|--attack-mode]}} 3 --increment {{hash_value}} "{{?a?a?a?a?a?a?a?a}}"`

- Կատարեք բառարանային հարձակում (ռեժիմ 0)՝ օգտագործելով բառացանկ.:

`hashcat {{[-m|--hash-type]}} {{hash_type_id}} {{[-a|--attack-mode]}} 0 {{hash_value}} {{path/to/wordlist.txt}}`

- Գործարկել բառարանի հարձակումը (ռեժիմ 0)՝ օգտագործելով նշված բառացանկը՝ կիրառելով կանոնների վրա հիմնված փոխակերպումներ՝ թեկնածուների գաղտնաբառերը փոխելու համար.:

`hashcat {{[-m|--hash-type]}} {{hash_type_id}} {{[-a|--attack-mode]}} 0 {{[-r|--rules-file]}} {{path/to/file.rule}} {{hash_value}} {{path/to/wordlist.txt}}`

- Կատարեք համակցված հարձակում (ռեժիմ 1)՝ օգտագործելով երկու տարբեր սովորական բառարանների բառերի միացումը.:

`hashcat {{[-m|--hash-type]}} {{hash_type_id}} {{[-a|--attack-mode]}} 1 {{hash_value}} {{path/to/dictionary1.txt}} {{path/to/dictionary2.txt}}`

- Ցույց տալ արդեն ճեղքված հեշի արդյունքը.:

`hashcat --show {{hash_value}}`

- Ցույց տալ բոլոր օրինակների հեշերը.:

`hashcat --example-hashes`

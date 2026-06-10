# rsql

> SQL հաճախորդը` տերմինալի ներսում տվյալների բազաների և տվյալների այլ աղբյուրների հետ ինտերֆեյսի համար:.
> Լրացուցիչ տեղեկություններ. <https://github.com/theseus-rs/rsql>:.

- Մուտքագրեք ինտերակտիվ ռեժիմ.:

`rsql`

- Միացեք տվյալների շտեմարանին (օրինակ՝ PostgreSQL).:

`rsql --url "{{postgresql://user:pass@localhost/mydb}}"`

- Միացեք PostgreSQL տվյալների բազային SSL-ով.:

`rsql --url "{{postgresql://user:pass@localhost/db?sslmode=require}}"`

- Միացեք MySQL տվյալների շտեմարանին նշված նիշերի հավաքածուով.:

`rsql --url "{{mysql://user:pass@localhost/db?charset=utf8mb4}}"`

- Կատարեք հարցում և դուրս եկեք.:

`rsql --url "{{sqlite://database.db}}" -- "{{SELECT * FROM users LIMIT 10}}"`

- Սահմանեք լռելյայն ձևաչափը.:

`rsql --url "{{sqlite://db.sqlite}}" --format json`

- Միացեք ֆայլին և օգտագործեք հատուկ տողերի բաժանարար.:

`rsql --url "{{delimited://data.txt?separator=|&has_header=true}}"`

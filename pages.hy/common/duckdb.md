# բադդբ

> Հաճախորդ DuckDB-ի համար, որը գործընթացում վերլուծական SQL շարժիչ է:.
> Լրացուցիչ տեղեկություններ. <https://duckdb.org/docs/stable/clients/cli/arguments>:.

- Սկսեք ինտերակտիվ վահանակ՝ անցողիկ հիշողության տվյալների բազայով.:

`duckdb`

- Սկսեք ինտերակտիվ վահանակ տվյալների բազայի ֆայլի վրա: Եթե ֆայլը գոյություն չունի, ստեղծվում է նոր տվյալների բազա.:

`duckdb {{path/to/dbfile}}`

- Հարցրեք CSV, JSON կամ մանրահատակի ֆայլ՝ օգտագործելով SQL:

`duckdb -c "{{SELECT * FROM 'data_source.[csv|csv.gz|json|json.gz|parquet]'}}"`

- Ուղղակի հարցումներ կատարեք CSV, JSON կամ Մանրահատակի ֆայլի միջոցով՝ օգտագործելով `file` դիտումը.:

`duckdb {{data_source.[csv|csv.gz|json|json.gz|parquet]}} -c "{{ SELECT * FROM file }}"`

- Գործարկել SQL սկրիպտը.:

`duckdb -f {{path/to/script.sql}}`

- Գործարկեք հարցումը տվյալների բազայի ֆայլում և բաց պահեք ինտերակտիվ կեղևը.:

`duckdb {{path/to/dbfile}} -cmd "{{SELECT DISTINCT * FROM tbl}}"`

- Կարդացեք CSV `stdin`-ից և գրեք CSV `stdout`-ում:

`cat {{path/to/source.csv}} | duckdb -c "{{COPY (FROM read_csv('/dev/stdin')) TO '/dev/stdout' WITH (FORMAT CSV, HEADER)}}"`

- Սկսեք DuckDB UI-ը, վեբ ինտերֆեյսը նոութբուքերով.:

`duckdb -ui`

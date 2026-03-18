# ghauri

> Detect and exploit SQL injection vulnerabilities.
> See also: `sqlmap`.
> More information: <https://github.com/r0oth3x49/ghauri>.

- Test a URL for SQL injection:

`ghauri {{[-u|--url]}} "{{http://example.com/page?id=1}}"`

- Test a URL with POST data:

`ghauri {{[-u|--url]}} "{{http://example.com/page}}" --data "{{id=1&name=test}}"`

- Specify the DBMS backend and test a specific parameter:

`ghauri {{[-u|--url]}} "{{http://example.com/page?id=1&name=test}}" --dbms {{MySQL}} -p {{id}}`

- Enumerate databases:

`ghauri {{[-u|--url]}} "{{http://example.com/page?id=1}}" --dbs`

- Dump a specific table from a database:

`ghauri {{[-u|--url]}} "{{http://example.com/page?id=1}}" -D {{database_name}} -T {{table_name}} --dump`

- Load a request from a file and use a proxy:

`ghauri -r {{path/to/request.txt}} --proxy {{http://127.0.0.1:8080}}`

- Set test level and specific SQL injection technique:

`ghauri {{[-u|--url]}} "{{http://example.com/page?id=1}}" --level {{3}} --technique {{BET}}`

- Use batch mode to accept default prompts automatically:

`ghauri {{[-u|--url]}} "{{http://example.com/page?id=1}}" --batch --dbs`

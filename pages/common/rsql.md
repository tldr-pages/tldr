# rsql

> SQL client to interface with databases and other data sources inside the terminal.
> More information: <https://github.com/theseus-rs/rsql>.

- Enter interactive mode:

`rsql`

- Connect to a database (es. PostgreSQL):

`rsql --url {{"postgresql://user:pass@localhost/mydb"}}`

- PostgreSQL with SSL:

`rsql --url {{"postgresql://user:pass@localhost/db?sslmode=require"}}`

- MySQL with charset:

`rsql --url {{"mysql://user:pass@localhost/db?charset=utf8mb4"}}`

- Run a query and exit (not in interactive mode):

`rsql --url {{"sqlite://database.db"}} -- "SELECT * FROM users LIMIT 10"`

- Set default format:

`rsql --url {{"sqlite://db.sqlite"}} --format json`

- Delimited file with custom separator (es .txt file):

`rsql --url {{"delimited://data.txt?separator=|&has_header=true"}}`

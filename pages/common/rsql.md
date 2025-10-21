# rsql

> SQL client to interface with databases and other data sources inside the terminal.
> More information: <https://github.com/theseus-rs/rsql>.

- Enter interactive mode:

`rsql`

- Connect to a database (e.g. PostgreSQL):

`rsql --url "{{postgresql://user:pass@localhost/mydb}}"`

- Connect to a PostgreSQL database with SSL:

`rsql --url "{{postgresql://user:pass@localhost/db?sslmode=require}}"`

- Connect to a MySQL database with a specified charset:

`rsql --url "{{mysql://user:pass@localhost/db?charset=utf8mb4}}"`

- Run a query and exit:

`rsql --url "{{sqlite://database.db}}" -- "SELECT * FROM users LIMIT 10"`

- Set default format:

`rsql --url "{{sqlite://db.sqlite}}" --format json`

- Connect to file and use custom line separator:

`rsql --url "{{delimited://data.txt?separator=|&has_header=true}}"`

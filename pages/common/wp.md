# wp

> The official command-line interface to manage WordPress instances.
> More information: <https://wp-cli.org/>.

- Print information about the operating system, shell, PHP, and WP-CLI (`wp`) installation:

`wp --info`

- Update WP-CLI:

`wp cli update`

- Download a fresh WordPress installation to current directory, optionally specifying the locale:

`wp core download --locale={{locale}}`

- Create basic `wpconfig` file (assuming database on `localhost`):

`wp config create --dbname={{dbname}} --dbuser={{dbuser}} --dbpass={{dbpass}}`

- Install and activate a WordPress plugin:

`wp plugin install {{plugin}} --activate`

- Replace all instances of a string in the database:

`wp search-replace {{old_string}} {{new_string}}`

- Import the contents of a WordPress Extended RSS (WXR) file:

`wp import {{path/to/file.xml}}`

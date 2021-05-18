# wp

> The official command-line interface to manage WordPress instances.
> More information: <https://wp-cli.org/>.

- Describe the operating system, shell, PHP, and WP-CLI (`wp`) installation:

`wp --info`

- Update WP-CLI:

`wp cli update`

- Install and activate a WordPress plugin:

`wp plugin install {{plugin}} --activate`

- Replace all instances of the old string in the database with the new string:

`wp search-replace {{old}} {{new}}`

- Import the contents of a WordPress Extended RSS (WXR) file:

`wp import {{path/to/file.xml}}`

# phpquery

> PHP extension manager for Debian-based OSes.
> More information: <https://helpmanual.io/help/phpquery/>.

- List available PHP versions:

`sudo phpquery -V`

- List available SAPIs for PHP 7.3:

`sudo phpquery -v {{7.3}} -S`

- List enabled extensions for PHP 7.3 with the cli SAPI:

`sudo phpquery -v {{7.3}} -s {{cli}} -M`

- Check if the JSON extension is enabled for PHP 7.3 with the apache2 SAPI:

`sudo phpquery -v {{7.3}} -s {{apache2}} -m {{json}}`

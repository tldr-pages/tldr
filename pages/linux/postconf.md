# postconf

> Postfix configuration utility.
> This command displays the values of the `main.cf` configuration parameters by default and warns about possible mistyped parameter names. It can also change the `main.cf` configuration parameter values.
> More information: <https://manned.org/postconf>.

- Specify the directory of the `main.cf` configuration file instead of the default configuration directory:

`postconf -c {{path/to/configuration_directory}}`

- Edit the `main.cf` configuration file and update parameter settings with the "name=value" pairs:

`postconf -e`

- Print the default parameter settings of the `main.cf` instead of the actual settings:

`postconf -d`

- Display parameters only from the specified class. The class can be one of builtin, service, user or all:

`postconf -C {{class}}`

- List available SASL plug-in types for the Postfix SMTP server. The plug-in type is selected with the `smtpd_sasl_type` configuration parameter by specifying `cyrus` or `dovecot` as the name:

`postconf -a`

- List the names of all supported lookup table types. Lookup tables are specified as `type:name` in configuration files where the type can be `btree`, `cdb`, `hash`, `mysql`, etc:

`postconf -m`

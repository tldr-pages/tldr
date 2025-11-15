# elasticsearch-keystore

> Manage secure settings (e.g., passwords, tokens, and credentials) used by Elasticsearch.
> More information: <https://www.elastic.co/guide/en/elasticsearch/reference/current/elasticsearch-keystore.html>.

- Create a new keystore (not password-protected):

`elasticsearch-keystore create`

- Create a new password-protected keystore:

`elasticsearch-keystore create -p`

- Add a setting interactively:

`elasticsearch-keystore add {{setting_name}}`

- Add a setting from `stdin`:

`echo "{{setting_value}}" | elasticsearch-keystore add --stdin {{setting_name}}`

- Remove a setting from the keystore:

`elasticsearch-keystore remove {{setting_name}}`

- Change the keystore password:

`elasticsearch-keystore passwd`

- List all settings stored in the keystore:

`elasticsearch-keystore list`

- Upgrade the keystore format (after an Elasticsearch upgrade):

`elasticsearch-keystore upgrade`

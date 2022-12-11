# twurl

> Curl-like command but tailored specifically for the Twitter API.
> More information: <https://github.com/twitter/twurl>.

- Authorize `twurl` to access a Twitter account:

`twurl authorize --consumer-key {{twitter_api_key}} --consumer-secret {{twitter_api_secret}}`

- Make a GET request to an API endpoint:

`twurl -X GET {{twitter_api_endpoint}}`

- Make a POST request to an API endpoint:

`twurl -X POST -d '{{endpoint_params}}' {{twitter_api_endpoint}}`

- Upload media to Twitter:

`twurl -H "{{twitter_upload_url}}" -X POST "{{twitter_upload_endpoint}}" --file "{{path/to/media.jpg}}" --file-field "media"`

- Access a different Twitter API host:

`twurl -H {{twitter_api_url}} -X GET {{twitter_api_endpoint}}`

- Create an alias for a requested resource:

`twurl alias {{alias_name}} {{resource}}`

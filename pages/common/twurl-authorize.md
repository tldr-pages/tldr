# twurl authorize

> Authorize twurl with Twitter API credentials.
> More information: <https://github.com/twitter/twurl>.

- Authorize twurl using a consumer key and secret:

`twurl authorize {{[-c|--consumer-key]}} {{consumer_key}} {{[-s|--consumer-secret]}} {{consumer_secret}}`

- Authorize twurl using a consumer key and secret, and open the authorization URL in a browser:

`twurl authorize {{[-c|--consumer-key]}} {{consumer_key}} {{[-s|--consumer-secret]}} {{consumer_secret}} --open`

- Authorize twurl for a specific host:

`twurl authorize {{[-c|--consumer-key]}} {{consumer_key}} {{[-s|--consumer-secret]}} {{consumer_secret}} {{[-H|--host]}} {{api.twitter.com}}`

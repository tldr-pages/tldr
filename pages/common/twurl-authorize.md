# twurl authorize

> Authorize twurl with Twitter API credentials.
> More information: <https://github.com/twitter/twurl>.

- Authorize twurl using a consumer key and secret:

`twurl authorize --consumer-key {{consumer_key}} --consumer-secret {{consumer_secret}}`

- Authorize twurl using a consumer key and secret, and open the authorization URL in a browser:

`twurl authorize --consumer-key {{consumer_key}} --consumer-secret {{consumer_secret}} --open`

- Authorize twurl for a specific host:

`twurl authorize --consumer-key {{consumer_key}} --consumer-secret {{consumer_secret}} --host {{api.twitter.com}}`

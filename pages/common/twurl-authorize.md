\# twurl authorize



> Authorize twurl with Twitter API credentials.

> More information: <https://github.com/twitter/twurl>.



\- Authorize twurl using a consumer key and secret:



`twurl authorize --consumer-key {{consumer\_key}} --consumer-secret {{consumer\_secret}}`



\- Authorize twurl using a consumer key and secret, and open the authorization URL in a browser:



`twurl authorize -c {{consumer\_key}} -s {{consumer\_secret}} --open`



\- Authorize twurl for a specific host:



`twurl authorize -c {{consumer\_key}} -s {{consumer\_secret}} -H {{api.twitter.com}}`


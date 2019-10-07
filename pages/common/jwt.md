# jwt

> `jwt-cli` is a command line tool to help you work with JSON Web Tokens (JWTs).
> A super fast CLI tool to decode and encode JWTs built in Rust.
> Encryption algorithms available are HS256,HS384, HS512, RS256, RS384, RS512, ES256, ES384.
> For more information: <https://github.com/mike-engel/jwt-cli>.

- Decode a JWT:

`jwt decode <JWT string>`

- Decode a JWT as JSON:

`jwt decode -j <JWT string>`

- Encode a JSON to JWT:

`jwt encode --alg <ALGO> --secret <SECRET> '<JSON>'`

- Encode key pair payload to JWT:

`jwt encode --alg <ALGO> --secret <SECRET> -P key=value`

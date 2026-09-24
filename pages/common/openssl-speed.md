# openssl speed

> Benchmark OpenSSL algorithms.
> More information: <https://docs.openssl.org/master/man1/openssl-speed/>.

- Benchmark all available algorithms:

`openssl speed`

- Benchmark the most common algorithms:

`openssl speed {{md5 sha1 sha256 aes rsa}}`

- Benchmark a specific EVP cipher:

`openssl speed -evp {{aes-256-cbc}}`

- Benchmark algorithms for a specific duration (in seconds):

`openssl speed -seconds {{10}}`

- Benchmark using wall-clock time instead of CPU user time:

`openssl speed -elapsed`

- Output in machine readable format:

`openssl speed -mr`

- Benchmark multiple algorithms in parallel using all available CPU cores:

`openssl speed -multi $(nproc)`

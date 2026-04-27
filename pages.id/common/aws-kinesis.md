# aws kinesis

> Berinteraksi dengan Amazon Kinesis Data Streams, suatu layanan yang memudahkan pemrosesan penyiaran big data secara segera dan elastis.
> Informasi lebih lanjut: <https://docs.aws.amazon.com/cli/latest/reference/kinesis/index.html#cli-aws-kinesis>.

- Tampilkan daftar seluruh siaran dalam akun yang masuk:

`aws kinesis list-streams`

- Tulis sebuah rekor dalam suatu siaran Kinesis:

`aws kinesis put-record --stream-name {{nama}} --partition-key {{kunci}} --data {{pesan_dalam_sandian_base64}}`

- Tulis sebuah rekor dalam suatu siaran Kinesis dengan menyandikan pesan base64 secara langsung dalam barisan perintah:

`aws kinesis put-record --stream-name {{nama}} --partition-key {{kunci}} --data "$( echo "{{pesan mentah saya}}" | base64 )"`

- Tampilkan daftar pecahan (shard) yang tersedia dalam suatu siaran:

`aws kinesis list-shards --stream-name {{nama}}`

- Dapatkan sebuah iterator pecahan untuk membaca dari pesan terlampau dalam suatu pecahan siaran:

`aws kinesis get-shard-iterator --shard-iterator-type TRIM_HORIZON --stream-name {{nama}} --shard-id {{id_pecahan}}`

- Baca kumpulan rekor dari suatu pecahan, menggunakan iterator pecahan:

`aws kinesis get-records --shard-iterator {{iterator}}`

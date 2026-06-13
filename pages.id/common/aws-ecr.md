# aws ecr

> Dorong, tarik, dan atur citra kontainer.
> Informasi lebih lanjut: <https://docs.aws.amazon.com/cli/latest/reference/ecr/>.

- Masuk ke dalam manajer Docker dengan registri default (username adalah AWS):

`aws ecr get-login-password --region {{wilayah}} | {{docker login}} --username AWS --password-stdin {{id_akun_aws}}.dkr.ecr.{{wilayah}}.amazonaws.com`

- Buat suatu repositori:

`aws ecr create-repository --repository-name {{repositori}} --image-scanning-configuration scanOnPush={{true|false}} --region {{wilayah}}`

- Tandai suatu citra lokal untuk ECR:

`docker tag {{nama_kontainer}}:{{tag}} {{id_akun_aws}}.dkr.ecr.{{wilayah}}.amazonaws.com/{{nama_kontainer}}:{{tag}}`

- Dorong suatu citra menuju suatu repositori:

`docker push {{id_akun_aws}}.dkr.ecr.{{wilayah}}.amazonaws.com/{{nama_kontainer}}:{{tag}}`

- Tarik suatu citra dari suatu repositori:

`docker pull {{id_akun_aws}}.dkr.ecr.{{wilayah}}.amazonaws.com/{{nama_kontainer}}:{{tag}}`

- Hapus suatu citra dalam suatu repositori:

`aws ecr batch-delete-image --repository-name {{repositori}} --image-ids imageTag={{latest}}`

- Hapus suatu repositori:

`aws ecr delete-repository --repository-name {{repositori}} --force`

- Tampilkan daftar citra dalam suatu repositori:

`aws ecr list-images --repository-name {{repositori}}`

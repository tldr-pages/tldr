# aws ec2

> Atur daftar instansi dan volume penyimpanan AWS EC2.
> AWS EC2 menyediakan kapasitas komputasi yang aman dan dapat diubah ukurannya dalam platform komputasi awan AWS untuk pengembangan dan penerapan aplikasi yang lebih cepat.
> Informasi lebih lanjut: <https://docs.aws.amazon.com/cli/latest/reference/ec2/>.

- Tampilkan informasi mengenai suatu instansi EC2:

`aws ec2 describe-instances --instance-ids {{id_instansi}}`

- Tampilkan informasi mengenai seluruh instansi EC2 terdaftar:

`aws ec2 describe-instances`

- Tampilkan informasi mengenai seluruh volume penyimpanan EC2 terdaftar:

`aws ec2 describe-volumes`

- Hapus suatu volume penyimpanan EC2:

`aws ec2 delete-volume --volume-id {{id_volume}}`

- Buat suatu tangkapan isi (snapshot) suatu volume penyimpanan EC2:

`aws ec2 create-snapshot --volume-id {{id_volume}}`

- Tampilkan daftar cakram AMI (Amazon Machine Image) yang tersedia:

`aws ec2 describe-images`

- Tampilkan seluruh perintah EC2 yang tersedia:

`aws ec2 help`

- Tampilkan bantuan spesifik untuk suatu subperintah EC2:

`aws ec2 {{subperintah}} help`

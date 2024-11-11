# aws acm

> AWS Certificate Manager, manajer sertifikat digital untuk AWS.
> Informasi lebih lanjut: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/index.html>.

- Impor suatu sertifikat:

`aws acm import-certificate --certificate-arn {{arn_sertifikat}} --certificate {{sertifikat}} --private-key {{kunci_privat}} --certificate-chain {{rantai_sertifikat}}`

- Tampilkan daftar sertifikat:

`aws acm list-certificates`

- Tampilkan deskripsi suatu sertifikat:

`aws acm describe-certificate --certificate-arn {{arn_sertifikat}}`

- Minta sertifikat baru bagi suatu domain:

`aws acm request-certificate --domain-name {{nama_domain}} --validation-method {{metode_validasi}}`

- Hapus suatu sertifikat:

`aws acm delete-certificate --certificate-arn {{arn_sertifikat}}`

- Tampilkan daftar status pengajuan validasi sertifikat:

`aws acm list-certificates --certificate-statuses {{status}}`

- Dapatkan informasi rincian suatu sertifikat:

`aws acm get-certificate --certificate-arn {{arn_sertifikat}}`

- Mutakhirkan pengaturan terhadap suatu sertifikat:

`aws acm update-certificate-options --certificate-arn {{arn_sertifikat}} --options {{pengaturan}}`

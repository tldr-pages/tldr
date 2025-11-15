# argon2

> Hitung kode hash menggunakan algoritma kriptografi Argon2.
> Informasi lebih lanjut: <https://github.com/P-H-C/phc-winner-argon2#command-line-utility>.

- Hitung kode hash dari suatu kata kunci (password) dengan suatu kata garam (salt) menggunakan parameter kriptografi bawaan:

`echo "{{kata_sandi}}" | argon2 "{{kata_garam}}"`

- Hitung kode hash dengan algoritma tertentu:

`echo "{{kata_sandi}}" | argon2 "{{kata_garam}}" -{{d|i|id}}`

- Jangan tampilkan informasi tambahan selain hasil kode hash:

`echo "{{kata_sandi}}" | argon2 "{{kata_garam}}" -e`

- Hitung kode hash dengan konfigurasi wak[t]u, pemanfaatan [m]emori (RAM), dan [p]aralelisme pada pemrosesan kriptografi secara tertentu:

`echo "{{kata_sandi}}" | argon2 "{{kata_garam}}" -t {{5}} -m {{20}} -p {{7}}`

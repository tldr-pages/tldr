# md5sum

> Calculați sumele de verificare criptografice MD5.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/md5sum>

- Calculați suma de control MD5 pentru un fișier:

`md5sum {{filename1}}`

- Calculați sumele de control MD5 pentru mai multe fișiere:

`md5sum {{filename1}} {{filename2}}`

- Citiți un fișier de MD5SUM și verificați toate fișierele au sume de control potrivite:

`md5sum -c {{filename.md5}}`

- Se calculează o sumă de control MD5 din intrarea standard:

`echo "{{text}}" | md5sum`

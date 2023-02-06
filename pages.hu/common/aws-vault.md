# aws-vault

> Az AWS hitelesítő adatok biztonságos tárolására és elérésére szolgáló páncélterem a fejlesztési környezetekben. További információ: <https://github.com/99designs/aws-vault>.

- Hitelesítési adatok hozzáadása a biztonságos keystore-hoz:

`aws-vault add {{profile}}`

- Végezzen parancsot AWS hitelesítő adatokkal a környezetben:

`aws-vault exec {{profile}} -- {{aws s3 ls}}`

- Nyisson meg egy böngészőablakot, és jelentkezzen be az AWS konzolba:

`aws-vault login {{profile}}`

- Profilok listázása a hitelesítő adatokkal és munkamenetekkel együtt:

`aws-vault list`

- AWS hitelesítő adatok forgatása:

`aws-vault rotate {{profile}}`

- Hitelesítési adatok eltávolítása a biztonságos keystore-ból:

`aws-vault remove {{profile}}`

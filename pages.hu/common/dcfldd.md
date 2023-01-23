# dcfldd

> A dd továbbfejlesztett változata a törvényszéki és biztonsági vizsgálatokhoz. További információ: <http://dcfldd.sourceforge.net/>.

- Lemez másolása nyers képfájlba, és a kép SHA256 segítségével történő kivonatolása:

`dcfldd if=/dev/{{disk_device}} of={{file.img}} hash=sha256 hashlog={{file.hash}}`

- Lemez másolása nyers képfájlba, minden egyes 1 GB-os darab hashelésével:

`dcfldd if=/dev/{{disk_device}} of={{file.img}} hash={{sha512|sha384|sha256|sha1|md5}} hashlog={{file.hash}} hashwindow={{1G}}`

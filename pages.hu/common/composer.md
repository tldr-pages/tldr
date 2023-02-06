# composer

> Csomag alapú függőségkezelő PHP projektekhez. További információ: <https://getcomposer.org/>.

- Interaktívan hozzon létre egy `composer.json` fájlt:

`composer init`

- Adjon hozzá egy csomagot függőségként ehhez a projekthez, hozzáadva azt a `composer.json`:

`composer require {{user/package_name}}`

- Telepítse az összes függőséget ebben a projektben `composer.json` és hozza létre a `composer.lock`:

`composer install`

- Eltávolít egy csomagot ebből a projektből, eltávolítva azt függőségként a `composer.json`:

`composer remove {{user/package_name}}`

- A projekt összes függőségének frissítése a `composer.json` oldalon, és a verziók feljegyzése a `composer.lock` fájlban:

`composer update`

- Csak a `composer.json` kézi frissítése után frissítse a composer lock-ot:

`composer update --lock`

- Tudjon meg többet arról, hogy egy függőség miért nem telepíthető:

`composer why-not {{user/package_name}}`

- A composer frissítése a legújabb verzióra:

`composer self-update`

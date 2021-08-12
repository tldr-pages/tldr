# composer

> Un manager de dependență bazat pe pachete pentru proiecte PHP.
> Mai multe informaţii: <https://getcomposer.org/>

- Crearea interactivă a unui fișier `composer.json':

`composer init`

- Adaugă un pachet ca dependență pentru acest proiect, adăugându-l la `composer.json`:

`composer require {{user/package_name}}`

- Instalați toate dependențele în `composer.json` al acestui proiect și creați `composer.lock`:

`composer install`

- Dezinstalați un pachet din acest proiect, eliminându-l ca o dependență de `composer.json`:

`composer remove {{user/package_name}}`

- Actualizați toate dependențele din `composer.json' și notați versiunile în fișierul `composer.lock`:

`composer update`

- Actualizați blocarea compozitorului numai după actualizarea manuală a `composer.json':

`composer update --lock`

- Aflați mai multe despre motivul pentru care o dependență nu poate fi instalată:

`composer why-not {{user/package_name}}`

- Actualizare compozitor la cea mai recentă versiune:

`composer self-update`

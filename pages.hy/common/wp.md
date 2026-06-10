# wp

> WordPress-ի օրինակները կառավարելու պաշտոնական ինտերֆեյսը:.
> Լրացուցիչ տեղեկություններ. <https://developer.wordpress.org/cli/commands/>:.

- Տպել տեղեկատվություն օպերացիոն համակարգի, shell-ի, PHP-ի և WP-CLI (`wp`) տեղադրման մասին.:

`wp --info`

- Թարմացրեք WP-CLI:

`wp cli update`

- Ներբեռնեք WordPress-ի թարմ տեղադրումը ընթացիկ գրացուցակում, կամայականորեն նշելով տեղայնությունը.:

`wp core download --locale={{locale}}`

- Ստեղծեք հիմնական `wpconfig` ֆայլ (ենթադրելով տվյալների բազա `localhost`-ում):

`wp config create --dbname={{dbname}} --dbuser={{dbuser}} --dbpass={{dbpass}}`

- Տեղադրեք և ակտիվացրեք WordPress հավելվածը.:

`wp plugin install {{plugin}} --activate`

- Փոխարինեք տվյալների բազայում տողի բոլոր օրինակները.:

`wp search-replace {{old_string}} {{new_string}}`

- Ներմուծեք WordPress Extended RSS (WXR) ֆայլի բովանդակությունը.:

`wp import {{path/to/file.xml}}`

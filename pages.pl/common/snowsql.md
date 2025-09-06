# snowsql

> Narzędzie wiersza SnowSQL serwisu bazodanowego Snowflake.
> Więcej informacji: <https://docs.snowflake.com/en/user-guide/snowsql.html>.

- Połącz z konkretną instancją pod adresem <https://konto.snowflakecomputing.com> (hasło może być wprowadzone w wierszu polecenia lub pliku konfiguracyjnym):

`snowsql --accountname {{konto}} --username {{użytkownik}} --dbname {{baza_danych}} --schemaname {{nazwa_schematu}}`

- Połącz się z instancją zdefiniowaną w pliku konfiguracyjnym (domyślnie w `~/.snowsql/config`):

`snowsql --config {{ścieżka/do/pliku_konfiguracyjnego}}`

- Połącz się z domyślnie zdefiniowaną instancją, podając kod autentykacji drugiego poziomu:

`snowsql --mfa-passcode {{kod_podwójnej_weryfikacji}}`

- Wykonaj pojedyncze zapytanie lub komendę SnowSQL na domyślnym połączeniu (użyteczne w skryptach powłoki):

`snowsql --query '{{zapytanie}}'`

- Wykonaj zapytania lub komendy z konkretnego pliku:

`snowsql --filename {{ścieżka/do/pliku.sql}}`

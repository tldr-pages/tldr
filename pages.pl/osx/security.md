# security

> Administruj pękami kluczy, kluczami, certyfikatami oraz framework'iem Security.
> Więcej informacji: <https://ss64.com/osx/security.html>.

- Wypisz wszystkie dostępne pęki kluczy:

`security list-keychains`

- Usuń zadany pęk kluczy:

`security delete-keychain {{ścieżka/do/pliku.keychain}}`

- Utwórz pęk kluczy:

`security create-keychain -p {{hasło}} {{ścieżka/do/pliku.keychain}}`

- Ustaw certyfikat który ma być używany przy stronie internetowej lub [s]erwisie używając nazwy własnej (ta komenda nie powiedzie się gdy więcej niż jeden certyfikat ma taką samą nazwę własną):

`security set-identity-preference -s {{URL|hostname|serwis}} -c "{{nazwa_własna}}" {{ścieżka/do/pliku.keychain}}`

- Dodaj certyfikat z pliku do pęku [k]luczy (Jeżeli parametr -k nie został podany, domyślny pęk kluczy zostanie wykorzystany):

`security add-certificates -k {{plik.keychain}} {{ścieżka/do/certyfikatu.keychain.pem}}`

- Dodaj certyfikat CA do ustawień zaufania dla każdego użytkownika:

`security add-trusted-cert -k {{ścieżka/do/pęku_kluczy_użytkownika.keychain-db}} {{ścieżka/do/certyfikatu_ca.pem}}`

- Usuń certyfikat CA z ustawień zaufania dla każdego użytkownika:

`security remove-trusted-cert {{ściieżka/do/certyfikatu_ca.pem}}`

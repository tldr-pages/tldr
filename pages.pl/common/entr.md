# entr

> Uruchom dowolną komendę, gdy zmieni się plik.
> Więcej informacji: <https://manned.org/entr>.

- Przebuduj projekt używając `make`, jeżeli zmiemi się którykolwiek z plików w podkatalogu:

`{{ag -l}} | entr {{make}}`

- Jeżeli zmieni się którykowliek z plików źródłowych `.c` w obecnym katalogu, przebuduj i uruchom testy używając `make`:

`{{ls *.c}} | entr {{'make && make test'}}`

- Wyślij `SIGTERM` do wszystkich uruchomionych poprzednio podprocesów ruby przed wykonaniem `ruby main.rb`:

`{{ls *.rb}} | entr -r {{ruby main.rb}}`

- Uruchom komendę przekazując zmieniony plik (`/_`) jako jej argument:

`{{ls *.sql}} | entr {{psql -f}} /_`

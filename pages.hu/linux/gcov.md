# gcov

> Kódlefedettség-elemző és profilalkotó eszköz, amely feltárja a program nem tesztelt részeit. Megjeleníti a forráskód másolatát is, a kódrészletek végrehajtási gyakoriságával megjegyezve. További információ: <https://gcc.gnu.org/onlinedocs/gcc/Invoking-Gcov.html>.

- Generálja a `file.cpp.gcov` nevű lefedettségi jelentést:

`gcov {{path/to/file.cpp}}`

- Írjon egyéni végrehajtási számokat minden egyes alapblokkhoz:

`gcov --all-blocks {{path/to/file.cpp}}`

- Elágazási gyakoriságok írása a kimeneti fájlba és az összefoglaló információk kiírása a `stdout` címre százalékos formában:

`gcov --branch-probabilities {{path/to/file.cpp}}`

- Az elágazási gyakoriságokat százalékos érték helyett a végrehajtott elágazások számaként írja ki:

`gcov --branch-counts {{path/to/file.cpp}}`

- Ne hozzon létre `gcov` kimeneti fájlt:

`gcov --no-output {{path/to/file.cpp}}`

- Írjon fájlszintű és függvényszintű összefoglalókat is:

`gcov --function-summaries {{path/to/file.cpp}}`

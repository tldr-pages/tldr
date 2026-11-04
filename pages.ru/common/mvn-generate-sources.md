# mvn generate-sources

> Генерировать исходный код для проекта Maven перед основной фазой компиляции.
> Эта фаза выполняется после `initialize` и перед `process-sources`.
> Больше информации: <https://manned.org/mvn>.

- Запустить все фазы жизненного цикла до `generate-sources`:

`mvn generate-sources`

- Запустить следующую фазу для генерации ресурсов:

`mvn generate-resources`

- Очистить и сгенерировать исходный код заново:

`mvn clean generate-sources`

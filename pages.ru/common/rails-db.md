# rails db

> Управлять базами данных в Ruby on Rails.
> Больше информации: <https://guides.rubyonrails.org/active_record_migrations.html>.

- Создать базы данных, загрузить схему и заполнить начальными данными:

`rails db:setup`

- Открыть консоль базы данных:

`rails db`

- Создать базы данных, определённые в текущем окружении:

`rails db:create`

- Удалить базы данных, определённые в текущем окружении:

`rails db:drop`

- Запустить ожидающие миграции:

`rails db:migrate`

- Показать статус каждого файла миграции:

`rails db:migrate:status`

- Откатить последнюю миграцию:

`rails db:rollback`

- Заполнить текущую базу данных данными, определёнными в `db/seeds.rb`:

`rails db:seed`

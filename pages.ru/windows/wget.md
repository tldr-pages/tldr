# wget

> В PowerShell эта команда может быть псевдонимом для `Invoke-WebRequest`, если оригинальная программа `wget` (<https://www.gnu.org/software/wget>) не установлена должным образом.
> Примечание: если команда вывода версии возвращает ошибку, PowerShell мог заменить эту команду на `Invoke-WebRequest`.
> Больше информации: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/invoke-webrequest>.

- Посмотреть документацию для оригинальной команды `wget`:

`tldr wget {{[-p|--platform]}} common`

- Посмотреть документацию для команды PowerShell `Invoke-WebRequest`:

`tldr invoke-webrequest`

- Проверить, правильно ли установлена программа `wget`, выведя номер её версии. Если выполнение этой команды завершается ошибкой, PowerShell мог заменить её на `Invoke-WebRequest`:

`wget --version`

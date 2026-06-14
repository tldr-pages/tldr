# git ֆիլտր-ճյուղ

> Փոխել մասնաճյուղի պատմությունը, օրինակ՝ ֆայլերը հեռացնելը:.
> Լրացուցիչ տեղեկություններ. <https://git-scm.com/docs/git-filter-branch>:.

- Հեռացրեք ֆայլը բոլոր պարտավորություններից.:

`git filter-branch --tree-filter 'rm {{[-f|--force]}} {{file}}' HEAD`

- Թարմացրեք հեղինակի էլ.:

`git filter-branch --env-filter 'GIT_AUTHOR_EMAIL={{new_email}}' HEAD`

- Ջնջել թղթապանակը պատմությունից.:

`git filter-branch --tree-filter 'rm {{[-rf|--recursive --force]}} {{folder}}' HEAD`

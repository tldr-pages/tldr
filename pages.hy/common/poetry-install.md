# պոեզիայի տեղադրում

> Տեղադրեք բոլոր կախվածությունները Python նախագծի համար, ինչպես սահմանված է pyproject.toml ֆայլում:.
> Լրացուցիչ տեղեկություններ. <https://python-poetry.org/docs/cli/#install>:.

- Տեղադրեք կախվածությունները.:

`poetry install`

- Բաց թողնել նախագիծն ինքնին որպես կախվածություն տեղադրելը.:

`poetry install --no-root`

- Տեղադրեք միայն արտադրական կախվածությունները.:

`poetry install --without dev`

- Տեղադրեք կամընտիր կախվածության խմբեր.:

`poetry install --with test,docs`

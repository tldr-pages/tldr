# venv

> Ստեղծեք թեթև վիրտուալ միջավայրեր Python-ում:.
> Լրացուցիչ տեղեկություններ. <https://docs.python.org/library/venv.html>:.

- Ստեղծեք Python վիրտուալ միջավայր.:

`python -m venv {{path/to/virtual_environment}}`

- Ակտիվացրեք վիրտուալ միջավայրը (Linux և macOS).:

`{{[.|source]}} {{path/to/virtual_environment}}/bin/activate`

- Ակտիվացրեք վիրտուալ միջավայրը (Windows).:

`{{path\to\virtual_environment}}\Scripts\activate.bat`

- Անջատեք վիրտուալ միջավայրը.:

`deactivate`

- Ստեղծեք կեղծանուն, որը ստեղծում է `venv` թղթապանակ և ինքնաբերաբար ակտիվացնում է այն.:

`alias venv='python -m venv .venv && source {{.venv/bin/activate|.venv\Scripts\activate.bat}}'`

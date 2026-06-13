# venv

> Maak lichtgewicht virtuele omgevingen in Python.
> Meer informatie: <https://docs.python.org/library/venv.html>.

- Maak een Python virtuele omgeving aan:

`python -m venv {{pad/naar/virtuele_omgeving}}`

- Activeer de virtuele omgeving (Linux en macOS):

`{{[.|source]}} {{pad\naar\virtuele_omgeving}}/bin/activate`

- Activeer de virtuele omgeving (Windows):

`{{pad\naar\virtuele_omgeving}}\Scripts\activate.bat`

- Deactiveer de virtuele omgeving:

`deactivate`

- Maak een alias aan die een `venv`-map genereert en deze automatisch activeert:

`alias venv='python -m venv .venv && source {{.venv/bin/activate|.venv\Scripts\activate.bat}}'`

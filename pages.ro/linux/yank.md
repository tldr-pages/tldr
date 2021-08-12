# yank

> Citiți intrarea din stdin și afișați o interfață de selecție care permite ca un câmp să fie selectat și copiat în clipboard.

- Yank folosind delimitatoarele implicite (\ f,\ n,\ r,\ s,\ t):

`{{sudo dmesg}} | yank`

- Yank o linie întreagă:

`{{sudo dmesg}} | yank -l`

- Yank folosind un delimitator specific:

`{{echo hello=world}} | yank -d {{=}}`

- Numai câmpurile yank care se potrivesc cu un anumit tipar:

`{{ps ux}} | yank -g "{{[0-9]+}}"`

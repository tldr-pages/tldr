# ansiweather

> Un script shell pentru afișarea condițiilor meteorologice curente în terminalul dvs.
> Mai multe informaţii: <https://github.com/fcambus/ansiweather>

- Afișează o prognoză utilizând unități metrice pentru următoarele cinci zile pentru Rzeszow, Polonia:

`ansiweather -u {{metric}} -f {{5}} -l {{Rzeszow,PL}}`

- Afișează o prognoză care afișează simboluri și date de lumină pentru locația curentă:

`ansiweather -s {{true}} -d {{true}}`

- Afișați o prognoză care arată datele despre vânt și umiditate pentru locația dvs. curentă:

`ansiweather -w {{true}} -h {{true}}`

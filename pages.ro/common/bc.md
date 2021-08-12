# bc

> Un limbaj de calculator de precizie arbitrar.
> Mai multe informaţii: <https://manned.org/bc>

- Porniți `BC' în modul interactiv folosind biblioteca de matematică standard:

`bc -l`

- Calculați rezultatul unei expresii:

`bc <<< "(1 + 2) * 2 ^ 2"`

- Calculați rezultatul unei expresii și forțați numărul de zecimale la 10:

`bc <<< "scale=10; 5 / 3"`

- Se calculează rezultatul unei expresii cu sinusul și cosinusul folosind `mathlib`:

`bc -l <<< "s(1) + c(1)"`

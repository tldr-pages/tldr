# let

> Evalueer rekenkundige uitdrukkingen in shell. 
> Meer informatie: <https://www.gnu.org/software/bash/manual/bash.html#index-let>.

- Evalueer een eenvoudige rekenkundige uitdrukking:

`let "{{result = a + b}}"`

- Gebruik post-increment en toewijzing in een uitdrukking:

`let "{{x++}}"`

- Gebruik een voorwaardelijke operator in een uitdrukking:

`let "{{result = (x > 10) ? x : 0}}"`

- Toon de help:

`let --help`

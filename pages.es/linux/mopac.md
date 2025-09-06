# mopac

> MOPAC (Molecular Orbital PACkage) es un programa semiempírico de química cuántica basado en la aproximación NDDO de Dewar y Thiel.
> Más información: <https://github.com/openmopac/mopac>.

- Realiza los cálculos a partir de un archivo de entrada (`.mop`, `.dat` y `.arc`):

`mopac {{ruta/al/archivo_de_entrada}}`

- Mínimo ejemplo de trabajo con HF que escribe en el directorio actual y lo guarda en el archivo de salida:

`touch test.out; echo "PM7\n#comment\n\nH 0.95506 0.05781 -0.03133\nF 1.89426 0.05781 -0.03133" > test.mop; mopac test.mop & tail -f test.out`

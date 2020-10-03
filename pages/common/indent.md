# indent

> Change the appearance of a C/C++ program by inserting or deleting whitespace.
> More information: <https://www.gnu.org/software/indent/>.

- Format C/C++ source according to the Linux style guide:

`indent -linux {{source1.c}} > {{source1.out}}`

- Format C/C++ source according to the GNU style:

`indent -gnu {{source2.c}} > {{source2.out}}`

- Format C/C++ source according to the style of Kernigan & Ritchie (K&R), no tabs, 3 spaces per indent, and wrap lines at 120 characters:

`indent -kr -i3 -nut -l120  {{source3.c}} > {{source3.out}}`

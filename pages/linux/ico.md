# ico

> Displays an animation of a polyhedron.
> More information: <https://manned.org/ico.1>.

- Display the wireframe of an icosahedron that changes its position every 0.1 seconds:

`ico -sleep {{0.1}}`

- Display a solid icosahedron with red faces on a blue background:

`ico -faces -noedges -colors {{red}} -bg {{blue}}`

- Display the wireframe of a cube with size 100x100 that moves by +1+2 per frame:

`ico -obj {{cube}} -size {{100x100}} -delta {{+1+2}}`

- Display the inverted wireframe of an icosahedron with line width 10 using 5 threads:

`ico -i -lw {{10}} -threads {{5}}`

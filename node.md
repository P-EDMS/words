#Node Structure

##Introduction

Although much of this book talks about graph data models, it is not a book about graph theory. We don’t need much theory to take advantage of graph databases: provided we understand what a graph is, we’re practically there. With that in mind, let’s refresh our memories about graphs in general.

- Node is an object.
- Object is something that posssesed attributes.
- Human made of atoms, EDMS made of nodes.

In a nutshell, graph comprises of:

- `vertex` -> `node`.
- `edge` -> `nodelink`.
- `graph` -> `node`. Graph is a node by itself.

##Graph

In EDMS, a graph can be regarded as a workspace.


**Limitation:**

- Only supported `1 to M` relationships to `Node`.

###data-structure

To represent `Graph` in data-structure:

Graph = {
  id, #node.id
  desc,
  mod, #what is this
  type #what is this
}

Graph is an extension to Node.


##Node

Just like atom, node is the most primitive building block in panton-core.

###data-structure

To represent `Node` in data-structure:

Node = {
  id,
  desc,
  createdAt,
  graphId, #node.id
  userId #node.id
}


##Node Link

Relationship is being treated as the fist-class citizen in graph-structure database. It connects 2 Nodes together.  

There are two types of graph in terms of node relationships:
- directed graph (digraph). A set of nodes connected by edges, where edges has direction associated with them.
- undirected graph.


In Panton, it adopted directed graph, and a direction from node A -> node B is represented by parent-child terminology.

From this structure, you may find that: 


###data-structure

NodeLink = {
  cNodeId, #node.id
  pNodeId, #node.id
  linkType #whats this?
}


##Extensions

Since `Node` is a generic structure, theoretically it can be inherited/extended. Its easy to do so in object-orietend(class) concept. But how do we implement in database table level?

Extension oftenly view as a collection of {param, value} pairs of a table. 

List of table extensions to node:
- graph
- fMedia
- nftEvent
- pIndex
- nodeAttribute

###data-structure
In order to extend a node structure in database table level, a new table(extension) must fulfill the following structure:

- maintain 1:1 relationship with node table.
- has `nodeId` as the primary key. (clone from node table's id field).

##Node Attribute
To support schema-less design in relational database.

Node attribute oftenly view as a collection of {param, value}  pairs of a node. 

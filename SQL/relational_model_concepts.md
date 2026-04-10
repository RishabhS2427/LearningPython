# Relational Model Concepts

Welcome to relational model concepts. After watching this video, you will be able to identify various set operations. Describe the properties and aspects of relations. Explain the difference between a relational schema, and a relational instance. Define relational terms such as degree and cardinality.

---

## Introduction to Relational Model
The relational model introduced in 1970 offers a powerful approach to organizing and understanding data. It centers around two fundamental concepts, sets and relations.

---

## Set Definition
Let us define each of these terms. A set is a collection of unique elements without a specified order, comprising items of a similar type, usually curly braces denote sets with the elements listed inside or described using set builder notation with a condition.

Sets play a critical role across various disciplines in modern mathematics, influencing algebra, geometry, and probability.

---

## Set Operations and Concepts

### Membership
Membership lowercase a is an element of uppercase A if an object A is an element of set A denoted by element a.

### Subset
A subset a is A subset of B. A set A is a subset of a set B. If every element of A is also an element of B by A subset B.

### Union
Union A union B the union of two sets A and B is the set of elements that are in A, in B, or both denoted by A union B.

### Intersection
Intersection A intersection B, the intersection of two sets A and B is the set of elements that are in both A and B, denoted by A intersection B.

### Difference
Difference A/B or A-B. The difference between two sets A and B is the set of elements that are in A but not in B.

### Empty Set
Empty set, the empty set denoted by curly brackets or the null sign, is a unique set having no elements and is a subset of every set.

---

## Additional Set Concepts

### Power Set
The power set of A is the set of all possible subsets of A, including the empty set and A itself, denoted by P parentheses A.

### Universal Set
The universal set, typically denoted by U, is the set that contains all objects under consideration and all other sets are subsets of it.

### Disjoint Sets
Disjoint sets, two sets are disjoint if they have no element in common.

### Venn Diagrams
Venn diagrams. These diagrams are visual representations of logical relations between sets.

---

## Relations
In addition to sets, the study of relations is essential, it is a mathematical concept based on the idea of sets. Relations describe connections between elements of sets and are crucial in set theory and logic.

---

### Types of Relations

#### Binary Relations
A binary relation establishes a connection between two elements. For instance, the less than relation illustrates the relationship between two numbers like 3 is less than 5.

#### Ordered Pairs
Ordered pairs a subset of the cartesian product A times B represent a binary relation on sets A and B, denoted as parentheses A comma B parentheses.

---

## Properties of Relations

### Reflexivity
The first property is reflexivity, a relation exhibits reflexivity when each element relates to itself. For instance, the equality relation equal exemplifies reflexivity as a equals a for any element a.

### Symmetry
The second property is symmetry. The property characterizes a relation of symmetric if whenever element a relates to b, b also relates to a. The is a sibling of relation serves as an example of symmetry.

### Transitivity
The next property is transitivity, which signifies that if element a is related to b and b is related to c, then a is also related to c. The less than relation displays transitivity, if a is less than b and b is less than c, then a is less than c.

### Antisymmetry
The last property is antisymmetry, it defines a relation as antisymmetric when a relates to b and b relates to a. Necessitating a to be equal to b, the less than or equal to relation demonstrates antisymmetry.

---

## Relation Schema and Instance

A relation consists of two essential components, the relation schema specifying the structure, and the relation instance representing the actual data.

### Relation Schema
A relation schema specifies the name of a relation and the name and type of each of the columns, which are the attributes. In this context, the entity author serves as an example. Author is the name of the relation, author_id is an attribute which can hold the data type char, which is a character string of a fixed length. Likewise, last name, first name, email, and city have the data type varchar, which is a character string of a variable link. The last attribute, country, also has a data type of char. This constitutes the relation schema.

### Relation Instance
The relation instance embodies the real world data stored in the table. A relation instance consists of rows and columns, the columns in the instance correspond to attributes, and the rows represent tuples, which are individual records.

---

## Key Concepts

### Degree
Degree represents the number of attributes or columns in a relation.

### Cardinality
Cardinality reflects the number of tuples or rows.

In the given example, the degree is 6, signifying the number of columns, while the cardinality is 5, indicating the count of tuples or rows.

---

## Summary
In this video, you learn that sets are collections without a specified order. Key set operations, including membership, subsets, union, and intersection, aid in understanding logical relations between sets. Relations describe connections between set elements, impacting set theory and logic. Common types of relation include binary relations and ordered pairs. A relation consists of two essential components, the relation schema and the relation instance. Degree indicates the number of columns, and cardinality is the count of row.
# ERDs and Types of Relationships

Welcome to ERDs and Types of Relationships.  After watching this video, you will be able to describe entity relationship diagram (ERD) and its fundamental components.  Identify the difference between one-to-one, one-to-many, and many-to-many relationships.

---

## ERD Definition
An ERD is a visual representation that illustrates the relationships and interactions between entities in a database.  It showcases the logical structure of a database system displaying entities and the relationships between them as lines connecting these boxes.

---

## Fundamental Components of Relationship
Let us now explore the fundamental components that form the structure of a relationship.  These include entities, relationship sets, and crow's foot notations.

---

### Entities
Entities in ERDs represent people, objects, or concepts that store data in a database.  They serve as fundamental building blocks depicted as rectangles in ERDs and contain attributes describing specific properties.  Entities form the basis for relationships within the database model.

---

### Relationship Sets
Relationship sets illustrate how entities are interconnected or associated with each other within a database.  They represent the connections between different entities, showing how instances of one entity type relate to instances of another entity type.

---

### Crow's Foot Notation
Crow's foot notation is a visual representation to indicate the relationship between entities in a database.  It employs symbols to signify the nature and quantity of relationships between entities.

These symbols provide a clear depiction of whether the relationship is one-to-one, one-to-many, or many-to-many, helping in the design and understanding of complex databases.

---

## Techniques for Representing Relationships
There are different techniques for representing relationships.

- A rectangle represents entity sets.  
- A diamond represents relationship sets with lines connecting associated entities.  
- The crow's foot notation employs symbols such as the greater-than symbol, the less-than symbol, and vertical lines to signify the nature and quantity of relationships between entities.  

---

## Attributes
In this example, the entity book is shown in a rectangle and the attributes are shown in oval.  Attributes are certain properties of that entity, for example, title, edition, year, price, and so on.

Each attribute connects to exactly one entity.

---

## Author Entity Example
Let's now see how the ER diagram appears for the author entity.  The entity author has attributes such as last name, first name, email, city, country, and author Id.

---

## Relationship Between Book and Author
Let's explore how the entities book and author relate to each other.

- A book requires at least one author, but can involve up to two authors or even more.  
- Similarly, an author can write one, two, or multiple books.  
- In both scenarios, a definitive relationship exists between the book and the author.  

---

## One-to-One Relationship
In this scenario, the relationship set is named "Authored by." Each book is written by a single author, denoted by the thick lines connecting the entities.  It represents a one-to-one relationship, implying that each entity in the set is engaged in at least one and precisely one relationship.

The diagrams only feature entities, as including attributes might clutter the diagram.

---

## One-to-Many Relationship
When multiple authors contribute to a book, it can be depicted using crow's foot notation using a less-than symbol.  The symbol signifies that one book entity is participating in multiple relationships within the set.  It is termed as a one-to-many relationship.

The relationship can also be viewed as a many-to-one signifying that multiple authors contribute to a single book.

---

## Many-to-Many Relationship
To represent many authors writing many books use the greater-than and less-than symbols on either side of the relationship set.  The scenario is termed a many-to-many relationship.  Multiple relationships involve each entity in the entity set.  It includes scenarios where many authors author many books.

---

## Summary
In this video, you learned that an ERD is a visual representation that illustrates the relationships and interactions between entities in a database.  The fundamental components that form the structure of a relationship include entities, relationship sets, and crow's foot notations.

- In a one-to-one relationship, each entity is linked to just one instance of another entity.  
- In a one-to-many relationship, an entity is linked with multiple instances of another entity.  
- In a many-to-many relationship, multiple instances of one entity are linked with multiple instances of another entity.  
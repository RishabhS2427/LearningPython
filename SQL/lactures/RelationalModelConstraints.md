# Relational Model Constraints

Welcome to Relational Model Constraints. After watching this video, you will be able to list the different types of relational model constraints, describe the different types of relational model constraints.

---

## Introduction

In a business, a data relational model needs to adhere to certain restrictions or rules.

In a relational data model, data integrity can be implemented using integrity rules or constraints.

The following six constraints are defined in a relational database model, entity integrity constraint, referential integrity constraint, semantic integrity constraint, domain constraint, null constraint, and check constraint.

---

## Entity Integrity Constraint

To identify each tuple in a relation, the relation must have a primary key.

The primary key is a unique value that identifies each tuple or row in a table.

This is the entity integrity constraint.

The terms primary key constraint or unique constraint are also used.

This constraint prevents duplicate values in a table.

To implement these constraints, indexes are used.

According to the entity integrity constraint, no attribute that is a part of the primary key of a relation should have null values.

The value null indicates that the value is unknown.

In the entity integrity constraint, the primary key cannot have an unknown value.

For example, in the relation author, author ID is the primary key.

The primary key identifies each tuple in the relation.

The author ID A1, points to author Raul Chong from Toronto.

If you replace the value A1 with null, you can still identify the author as Raul Chong.

However, if you also replace author ID A4 with null, now you do not know which null value identifies which tuple.

With the entity integrity constraint, no attribute participating in the primary key is allowed to accept null values.

---

## Referential Integrity Constraint

Relationships between tables are defined by the referential integrity constraint.

This constraint endorses the relationships between tables.

The validity of the data is enforced using a combination of primary keys and foreign keys.

As mentioned previously, for a book to exist, it has to be written by at least one author.

---

## Semantic Integrity Constraint

The correctness of the data in a table is enforced by the semantic integrity constraint.

For example, in the relation author, if the attribute or column city contains a garbage value instead of Toronto, the garbage value does not have any meaning.

The semantic integrity constraint is related to the correctness of the data.

---

## Domain Constraint

A domain constraint checks for valid values for a given attribute.

For example, in the relation author, the attribute country must contain a two letter country code, such as CA for Canada or IN for India.

If a number value of 34 is entered for the country attribute, instead of a two-letter country code, the value 34 does not have any meaning.

---

## Null Constraint

As observed earlier, the entity integrity constraint states that no attribute that is part of the primary key should accept null values.

The null constraint ensures that attribute values should not be null.

For example, in the relation author, if either last name or first name contains a null value, it could be difficult to identify the correct author.

In this example, first name and last name attribute values cannot be null.

An author must have a name.

---

## Check Constraint

The check constraint enforces domain integrity by limiting the values that are accepted by an attribute.

In the relation book, the attribute year is the year in which a particular book is published.

If this was still the year 2010, it would not be meaningful to have a year greater than the current year.

The check constraint would enforce the domain integrity by limiting the values that are accepted by the attribute year.

---

## Summary

In this video, you learned that entity integrity constraint checks that the value in the primary key is a unique value which identifies each tuple or row.

Referential Integrity constraint specifies the relationships which exist between tables.

Semantic integrity constraint enforces the correctness of the meaning of the data.

Domain constraint ensures that valid values are entered for a given attribute.

Null constraint ensures that attribute values should not be null.

Check constraint limits the values that are accepted by an attribute.
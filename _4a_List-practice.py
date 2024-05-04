# Example 1: Sorting by multiple keys
# Suppose you have a list of tuples representing people with their names, ages, and heights. You want to sort the list first by age,
# and then by height for people of the same age. Here's how you can do it using a custom sort key:

people = [("Alice", 25, 170), ("Bob", 20, 175), ("Charlie", 30, 160), ("Dave", 25, 180)]
sorted_people = sorted(people, key=lambda x: (x[1], -x[2]))
print(sorted_people) # [('Bob', 20, 175), ('Dave', 25, 180), ('Alice', 25, 170), ('Charlie', 30, 160)]

# The lambda function takes a tuple x as its argument and returns a tuple of two values: the age (x[1]) and the
# negative height (-x[2]). By negating the height, we ensure that the list is sorted in
# descending order by height for people of the same age. The resulting sorted_people list is:
# =============================================================================================================================================

# Example 2: Sorting by a computed value
# Suppose you have a list of tuples representing products with their names, prices, and quantities. You want to sort the list by the total value of
# each product (i.e., price multiplied by quantity). Here's how you can do it using a custom sort key:

products = [("Apple", 0.5, 10), ("Banana", 0.2, 20), ("Cherry", 1.5, 5)]
sorted_products = sorted(products, key=lambda x: x[1] * x[2])
print(sorted_products)

# The lambda function takes a tuple x as its argument and returns the computed value of the product (i.e., price multiplied by quantity) x[1] * x[2].

# =============================================================================================================================================
# Example 3: Sorting by a function of a value
# Suppose you have a list of tuples representing students with their names and exam scores. You want to sort the list by the percentage score of
# each student (i.e., score divided by maximum score). Here's how you can do it using a custom sort key:

students = [("Alice", 80), ("Bob", 60), ("Charlie", 90)]
max_score = 100
sorted_students = sorted(students, key=lambda x: x[1] / max_score, reverse=True)
print(sorted_students)

# The lambda function takes a tuple x as its argument and returns the percentage score of the student x[1] / max_score.
# We also set the reverse parameter to True to sort the list in descending order of percentage score.

# =============================================================================================================================================
# Example 4: Sorting by a value in a nested tuple
# Suppose you have a list of tuples representing employees with their names and salaries, and each employee also has a tuple of their job title and department.
# You want to sort the list by the salary of each employee, but you only want to consider employees in the "Sales" department.

employees = [("Alice", 50000, ("Manager", "Sales")), ("Bob", 40000, ("Salesperson", "Sales")), ("Charlie", 60000, ("Engineer", "Engineering")), ("Dave", 45000, ("Salesperson", "Marketing"))]
sorted_employees = sorted([e for e in employees if e[2][1] == "Sales"], key=lambda x: x[1])
print(sorted_employees)

# In this example, we use a list comprehension to filter out the employees who are not in the "Sales" department. Then, we use a lambda function as the key
# parameter of the sorted() function. The lambda function takes a tuple x as its argument and returns the salary of the employee x[1].

# =============================================================================================================================================
# Example 5: Sorting by a value in a dictionary
# Suppose you have a list of dictionaries representing books with their titles, authors, and publication years. You want to sort the list by the publication year of each book.

books = [{"title": "1984", "author": "George Orwell", "year": 1949}, {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932}, {"title": "Fahrenheit 451", "author": "Ray Bradbury", "year": 1953}]
sorted_books = sorted(books, key=lambda x: x["year"])
print(sorted_books)

# The lambda function takes a dictionary x as its argument and returns the publication year of the book x["year"].

# =============================================================================================================================================

# =============================================================================================================================================

# =============================================================================================================================================

# =============================================================================================================================================

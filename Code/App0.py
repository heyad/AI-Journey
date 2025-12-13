# Simple Python program to demonstrate working with lists

# Create a list of student names
students = ["Alice", "Bob", "Charlie", "Diana"]

# Print the list
print("Original list of students:", students)

# Add a new student to the list
students.append("Eve")
print("After adding a new student:", students)

# Remove a student from the list
students.remove("Bob")
print("After removing a student:", students)

# Access a specific student by index
print("The first student in the list is:", students[0])

# Sort the list alphabetically
students.sort()
print("Sorted list of students:", students)

# Find the total number of students
print("Total number of students:", len(students))
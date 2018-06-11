# Initializing sets from list of values
engineers = set(['John', 'Jane', 'Jack', 'Janice'])
programmers = set(['Jack', 'Sam', 'Susan', 'Janice'])
managers = set(['Jane', 'Jack', 'Susan', 'Zack'])

# Sample Union
employees = engineers | programmers | managers
print ('Employees')
print (employees)
print (' ')

# Sample Intersection
management_engineers = engineers & managers
print ('Management Engineers')
print (management_engineers)
print (' ')

# Sample Difference
fulltime_management = managers - engineers - programmers
print ('Fulltime Management')
print (fulltime_management)
print (' ')
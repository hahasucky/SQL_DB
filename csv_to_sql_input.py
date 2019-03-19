# script to turn my spread sheet to sql tuple input
# string syntax is as below :
# insert into instructor values (‘10211’, ’Smith’, ’Biology’, 66000);

#module csv import : to load from .csv files table input
import csv


# department input maker
print('\n\ndepartment input')

dept_f_id = open('/Users/sucky/Desktop/dept_input.csv', 'r')
rdr = csv.reader(dept_f_id)
department_input_lists = []
for line in rdr :
    str_to_convert = line.pop()
    num2put = int(str_to_convert)
    line.append(num2put)
    tuple_for_str_insert = tuple(line)
    final_str = 'insert into department values {};'.format(tuple_for_str_insert)
    department_input_lists.append(final_str)

for i in department_input_lists:
    print(i)


# instructor input maker
print('\n\ninstructor input')

instructor_f_id = open('/Users/sucky/Desktop/instructor_input.csv', 'r')
rdr = csv.reader(instructor_f_id)
instructor_input_lists = []
for line in rdr :
    last_element = line.pop()
    last_element_to_int = int(last_element)
    line.append(last_element_to_int)
    line_to_tuple = tuple(line)
    instructor_input_repr = 'insert into instructor values {};'.format(line_to_tuple)
    instructor_input_lists.append(instructor_input_repr)

instructor_f_id.close()
for i in instructor_input_lists :
    print(i)

# student input maker
print('\n\nstudent input')

student_f_id = open('/Users/sucky/Desktop/student_input.csv', 'r')
rdr = csv.reader(student_f_id)
student_input_lists = []
for line in rdr :
    str_to_convert = line.pop()
    num2put = int(str_to_convert)
    line.append(num2put)
    tuple_for_str_insert = tuple(line)
    final_str = 'insert into student values {};'.format(tuple_for_str_insert)
    student_input_lists.append(final_str)

for i in student_input_lists:
    print(i)

# course input maker
print('\n\ncourse input')

course_f_id = open('/Users/sucky/Desktop/course_input.csv', 'r')
rdr = csv.reader(course_f_id)
course_input_lists = []
for line in rdr :
    str_to_convert = line.pop()
    num2put = int(str_to_convert)
    line.append(num2put)
    tuple_for_str_insert = tuple(line)
    final_str = 'insert into course values {};'.format(tuple_for_str_insert)
    course_input_lists.append(final_str)

for i in course_input_lists:
    print(i)

# classroom input maker
print('\n\nclassroom input')

classroom_f_id = open('/Users/sucky/Desktop/classroom_input.csv', 'r')
rdr = csv.reader(classroom_f_id)
classroom_input_lists = []
for line in rdr :
    str_to_convert = line.pop()
    num2put = int(str_to_convert)
    line.append(num2put)
    tuple_for_str_insert = tuple(line)
    final_str = 'insert into classroom values {};'.format(tuple_for_str_insert)
    classroom_input_lists.append(final_str)

for i in classroom_input_lists:
    print(i)

# timeslot input maker
print('\n\ntime_slot input')

time_slot_f_id = open('/Users/sucky/Desktop/time_slot_input.csv', 'r')
rdr = csv.reader(time_slot_f_id)
time_slot_input_lists = []
for line in rdr :
    tuple_for_str_insert = tuple(line)
    final_str = 'insert into time_slot values {};'.format(tuple_for_str_insert)
    time_slot_input_lists.append(final_str)

for i in time_slot_input_lists:
    print(i)

# timeslot input maker
# classroom input maker
print('\n\nsection input')

section_f_id = open('/Users/sucky/Desktop/section_input.csv', 'r')
rdr = csv.reader(section_f_id)
section_input_lists = []
for line in rdr :
    str_to_convert = line.pop(3)
    num2put = int(str_to_convert)
    line[3] = num2put
    tuple_for_str_insert = tuple(line)
    final_str = 'insert into section values {};'.format(tuple_for_str_insert)
    section_input_lists.append(final_str)

for i in section_input_lists:
    print(i)


print('\n\nteaches input')

section_f_id = open('/Users/sucky/Desktop/teaches_input.csv', 'r')
rdr = csv.reader(section_f_id)
section_input_lists = []
for line in rdr :
    str_to_convert = line.pop()
    num2put = int(str_to_convert)
    line[-1] = num2put
    tuple_for_str_insert = tuple(line)
    final_str = 'insert into teaches values {};'.format(tuple_for_str_insert)
    section_input_lists.append(final_str)

for i in section_input_lists:
    print(i)


print('\n\ntakes input')

section_f_id = open('/Users/sucky/Desktop/takes_input.csv', 'r')
rdr = csv.reader(section_f_id)
section_input_lists = []
for line in rdr :
    str_to_convert = line.pop(0)
    new_str = str_to_convert.replace('\'','')
    line.insert(0, new_str)
    year_as_str = line.pop(4)
    int_year = int(year_as_str)
    line[4] = int_year
    tuple_for_str_insert = tuple(line)
    final_str = 'insert into takes values {};'.format(tuple_for_str_insert)
    section_input_lists.append(final_str)

for i in section_input_lists:
    print(i)







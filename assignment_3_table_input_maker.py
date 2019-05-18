def input_maker (grade, point):
	input_repr = "insert into grade_point values ({}, {});".format(grade, point)
	return input_repr


credit = ["'A+'","'A0'","'A-'","'B+'","'B0'","'B-'","'C+'","'C0'","'C-'"]
conv_str = [4.3, 4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7]

for i in range(len(credit)):
	command = input_maker(credit[i], conv_str[i])
	print(command)

print('sql is easy')

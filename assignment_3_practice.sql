# instructor join teaches using (id) join

SELECT DISTINCT ID
FROM takes
WHERE (course_id, sec_id, semester, year)
in
(SELECT course_id, sec_id, semester, year
FROM instructor JOIN teaches USING(ID)
WHERE name = 'Einstein');


SELECT ID,name
FROM instructor
WHERE salary =
(SELECT max(salary)
FROM instructor);


WITH total_enrollment_table AS
(SELECT count(ID) AS total_enrollment
FROM takes
WHERE semester = 'Fall' and year = 2009
GROUP BY (course_id, sec_id))
SELECT max(total_enrollment)
FROM total_enrollment_table;


SELECT course_id, sec_id
FROM takes
WHERE semester = 'Fall' and year = 2009
GROUP BY (course_id, sec_id)
HAVING count(ID) IN 
(
WITH total_enrollment_table AS
(SELECT count(ID) AS total_enrollment
FROM takes
WHERE semester = 'Fall' and year = 2009
GROUP BY (course_id, sec_id))
SELECT max(total_enrollment)
FROM total_enrollment_table
);




CREATE TABLE grade_point
(
grade varchar(2),
cvd_point numeric(3,1),
primary key(grade)
);



/*PRACTICE2-(3)*/
WITH A AS
(
/*sum of the grade point of 12345 table*/
WITH grade_point_per_sec_table AS
(SELECT credits*cvd_point as grade_point_per_sec 
FROM takes JOIN course USING(course_id)
	JOIN grade_point USING (grade)
WHERE ID = '12345')
SELECT sum(grade_point_per_sec)
FROM grade_point_per_sec_table
),
B AS
(
/*sum of the credits of 12345*/
SELECT sum(credits)
FROM takes JOIN course USING(course_id)
	JOIN grade_point USING (grade)
WHERE ID = '12345'
)
SELECT ROUND(A.sum/B.sum, 2) AS GPA
FROM A,B;

/*PRACTICE2 -(4)*/
/*c. Find the ID and the grade-point average of every student
2번 문항은 강의를 아무것도 듣지 않는 학생의 결과가 0이 나와야 하는 것에 유의하세요.*/
WITH GPA_TABLE AS (SELECT ID, SUM(cvd_point*credits)/SUM(credits) AS GPA
FROM student LEFT JOIN takes USING(ID)
	LEFT JOIN grade_point USING(grade)
		LEFT JOIN course USING(course_id)
GROUP BY(ID))
SELECT ID, ROUND(COALESCE(gpa, 0),2) AS GPA_
FROM GPA_TABLE
ORDER BY gpa_ DESC;



DELETE FROM course
WHERE course_id not in
(SELECT course_id
FROM section);



WITH ROOKIES AS
(SELECT ID, name, dept_name, 30000 as salary
FROM student
WHERE tot_cred > 100)
INSERT INTO instructor
SELECT * FROM ROOKIES;












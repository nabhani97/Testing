USE My_City_Students
GO 


-- practice
SELECT s.FirstName, s.Phone
FROM dbo.Student AS s

SELECT l.FirstName, l.Email
FROM dbo.Lecturer AS l



--1.	Show the course codes and descriptions for all courses.
SELECT c.CourseCode, c.CourseDescription
FROM Course as c

--2.   Show all details of every module with an exam weight of greater than or equal to 50% and with module convenor code 021478P.
Select *
From dbo.Module
Where ExamWeight >= 50 AND ModuleConvenor = '021478P'

--3.	Show all students (ID, first name and surname) taking Business Studies (course code BS).
SELECT s.StudentID, s.FirstName, s.Surname, sc.CourseCode		-- added the course code column for verification
FROM dbo.Student as s
Left Outer Join dbo.StudentCourse as sc
	on s.StudentID = sc.StudentID
Where CourseCode = 'BS'

--4.    Show all students (ID, first name and surname) taking Business Studies (course code BS) and module BS2029.
SELECT s.StudentID, s.FirstName, s.Surname, sc.CourseCode, sm.ModuleID
FROM dbo.Student as s
Left Outer Join dbo.StudentCourse as sc
	on s.StudentID = sc.StudentID
Left outer Join dbo.StudentModule as sm
	on s.StudentID = sm.StudentID
WHERE sm.CourseCode = 'BS' AND sm.ModuleID = 'BS2029'

--5.	Show all students (ID, first name and surname) who come from London, 
--but only if they are taking the Business Studies or Computer Science course (be sure to include your test data for this query in your submission).

SELECT s.StudentID, s.FirstName, s.Surname, sc.CourseCode, s.Town
FROM dbo.Student as s
Left Outer Join dbo.StudentCourse as sc
	on s.StudentID = sc.StudentID
left outer Join dbo.StudentModule as sm
	on s.StudentID = sm.StudentID
WHERE s.Town = 'London' AND (sm.CourseCode = 'BS' OR sm.CourseCode = 'CS')

--6.	Show all courses and associated modules (course code, description and module ID), even if the course has not yet been allocated any modules.

select c.coursecode, c.coursedescription, cm.moduleid
from dbo.Course as c
left outer join dbo.CourseModule as cm
	on c.CourseCode = cm.CourseCode


--7.	Show all courses and associated modules (course code, description, module ID and module description), even if the course has not yet been allocated any modules.
select c.coursecode, c.coursedescription, cm.moduleid, m.ModuleDescription
from dbo.Course as c
left outer join dbo.CourseModule as cm
	on c.CourseCode = cm.CourseCode
left outer join dbo.Module as m
	on cm.ModuleID = m.ModuleID

--8.	Show lecturer ID and names and their associated modules and also show all modules not assigned to any lecturer.
select l.StaffID, l.FirstName, l.Surname, sm.ModuleID, m.ModuleDescription
from Lecturer as l
left outer join StudentCourse as sc
	on l.StaffID = sc.Tutor
right outer join dbo.StudentModule as sm
	on sc.StudentID = sm.StudentID
left outer join dbo.Module as m
	on sm.ModuleID = m.ModuleID


--9.	Show the IDs and names of all students, and their average exam and coursework marks (with suitable headings).

Select s.StudentID, s.StudentID, AVG(sm.ExamMark) as 'AVGExamMark', avg(sm.cwmark) as 'AVGCWMark'
FROM dbo.Student as s
left outer join dbo.StudentModule as sm
	on s.StudentID = sm.StudentID
Group BY s.StudentID, s.StudentID

--10.	As exercise 9, but only those students with an average exam mark of 60% or more and only show the first character of their first name.
Select s.StudentID, s.StudentID, LEFT(s.FirstName, 1) as 'FirstInitial', AVG(sm.ExamMark) as 'AVGExamMark', avg(sm.cwmark) as 'AVGCWMark'
FROM dbo.Student as s
left outer join dbo.StudentModule as sm
	on s.StudentID = sm.StudentID
Group BY s.StudentID, s.StudentID,LEFT(s.FirstName, 1)
Having AVG(sm.exammark) >=60

--11.	Show the course codes and descriptions and the average exam and course weights of their associated modules, 
--but only where their average exam weight is 40% or more. Sort by course description, which should be shown in upper case.

select c.CourseCode, upper(c.CourseDescription), cm.ModuleID, AVG(m.examweight) as 'ExamWeight', AVG(m.CWWeight) as 'CWWeight'
from dbo.Course as c
left outer join dbo.CourseModule as cm
	on c.CourseCode = cm.CourseCode
left outer join dbo.Module as m
	on cm.ModuleID = m.ModuleID
Group By c.CourseCode, c.CourseDescription, cm.ModuleID
Having AVG(m.examweight) >= 40
order by c.CourseDescription ASC

--12.	Show the lecturer ID and name and the average exam and course work marks from all their modules, 
--but only where either average exam or coursework mark falls below 55%.  Restrict the search to non-excluded students and sort by lecturer surname.

Select l.StaffID, l.FirstName, l.Surname, m.ModuleID, s.StudentID, s.Excluded, avg(sm.ExamMark) as 'ExamMarkAVG', avg(sm.CWMark) as 'CWMarkAVG'
from dbo.Lecturer as l
full join dbo.Module as m
	on l.StaffID = m.ModuleConvenor
full join dbo.StudentModule as sm
	on m.ModuleID = sm.ModuleID
full join dbo.Student as s
	on sm.StudentID = s.StudentID
group by l.StaffID, l.FirstName, l.Surname, m.ModuleID, s.StudentID, s.Excluded
having s.Excluded = 1 AND (avg(sm.exammark) <55 OR AVG(sm.cwmark) <55)
order by l.Surname asc


--13.	Show the Lecturer ID and name, module ID and average coursework mark for each module that each lecturer has taken, ordered by lecturer name.

select l.FirstName, l.Surname, l.StaffID, m.ModuleID, avg(sm.CWmark) as 'AVGCWMark'
from dbo.Lecturer as l
full join dbo.Module as m
	on l.StaffID = m.ModuleConvenor
full join dbo.StudentModule as sm
	on m.ModuleID = sm.ModuleID
group by l.FirstName, l.Surname, l.StaffID, m.ModuleID
order by l.FirstName asc



-- nested queries, the bottom  here is all you need
Select MAX(sm.ExamMark) From dbo.StudentModule as sm

Select s.StudentID, s.Surname, sm.ModuleID, sm.ExamMark
From dbo.Student as s
Join dbo.StudentModule as sm
	on s.StudentID = sm.StudentID
where sm.ExamMark = (Select MAX(sm.ExamMark) From dbo.StudentModule as sm)


-- using = is for more only 1 equal
select s.studentIS, s.surname
from dbo.Student as s
join dbo.StudentModule as sm
	on Student

-- using IN returns the list of all instances
select s.firstname, s.surname
from dbo.Student as s
where s.StudentID IN (SElect sm.StudentID from dbo.studentmodule as sm where sm.ModuleID = 'bs2013')

select * from dbo.studentmodule

SELECT StudentID, MIN(sm.ExamMark)
FROM dbo.StudentModule AS sm 
GROUP BY StudentID


-- correlated query - find the min exam mark for each student and return that row of data basically
SELECT sm1.StudentID, sm1.ModuleID, sm1.ExamMark
FROM dbo.StudentModule AS sm1
WHERE sm1.ExamMark = (SELECT MIN(sm2.ExamMark)
			           FROM dbo.StudentModule AS sm2
			           WHERE sm2.StudentID = sm1.StudentID)

-- a variant of the correlated query above
SELECT s.StudentID, s.Surname, s.FirstName, s.Phone, 
       (SELECT MIN(sm1.ExamMark)
	 	 FROM dbo.StudentModule AS sm1
	 	 WHERE sm1.StudentID = s.StudentID) AS 'Min Exam Mark'
FROM dbo.Student AS s



--Worksheet 7 and 8

-- 1.	Select all students with a lower than average Exam mark, showing their name, ID and exam mark.
Select avg(sm.ExamMark) From dbo.StudentModule as sm

Select s.StudentID, s.Surname, sm.ModuleID, sm.ExamMark
From dbo.Student as s
Join dbo.StudentModule as sm
	on s.StudentID = sm.StudentID
where sm.ExamMark < (Select avg(sm.ExamMark) From dbo.StudentModule as sm)

-- 2.	Show the lecturer(s) with the highest exam weighting for a module.

Select * from Lecturer
Select * from StudentModule
select * from CourseModule
select * from StudentCourse

Select max(m.examweight) From dbo.Module as m

Select l.firstname, l.staffid, m.ExamWeight
From dbo.Lecturer as l
Join dbo.StudentCourse as sc
	on l.StaffID = sc.Tutor
join dbo.CourseModule as cm
	on sc.CourseCode = cm.CourseCode
join Module as m
	on cm.ModuleID = m.ModuleID
where m.Examweight in (Select max(m.examweight) From dbo.Module as m)


--3.	Select all courses where an ‘A’ has been awarded, showing course code and description. Do this using both a (a) nested query and (b) joins.
-- b) joins
Select sm.Grade, c.CourseDescription, c.CourseCode
from dbo.StudentModule as sm
join dbo.Course as c
	on sm.CourseCode = c.CourseCode
where sm.Grade = 'A'

-- a) nested query
Select c.CourseDescription, c.CourseCode
from dbo.Course as c
where c.CourseCode IN (SElect CourseCode from dbo.StudentModule as sm where sm.Grade = 'A')


--4.	Show each lecturer’s lowest coursework weighting, displaying the Staff ID, the Module ID and the weighting selected.
SELECT l.staffID, m.ExamWeight, m.ModuleID
FROM dbo.Lecturer AS l
join dbo.Module as m
	on l.StaffID = m.ModuleConvenor
WHERE  m.ExamWeight in (SELECT MIN(m1.ExamWeight)
			           FROM dbo.Module AS m1 where m.ModuleConvenor = m1.ModuleConvenor)



-- derived query for: We want the Student IDs of all Students who have taken both Module 'M101' and Module 'M102'. This again at first sight might seem straightforward – 
-- we just have a complex filter condition on our hands. The query to produce the desired result might look something like this: (although in rl u wont use this, but makes sense)

SELECT s.StudentID, s.Surname, s.FirstName
FROM dbo.Student AS s
JOIN (SELECT s1.StudentID
      FROM dbo.Student AS s1
      INNER JOIN dbo.StudentModule AS sm
	       ON s1.StudentID = sm.StudentID
      WHERE sm.ModuleID = 'M101') AS mod1
ON s.StudentID = mod1.StudentID
JOIN (SELECT s2.StudentID
      FROM dbo.Student AS s2
      INNER JOIN dbo.StudentModule AS sm
	       ON s2.StudentID = sm.StudentID
      WHERE sm.ModuleID = 'M102') AS mod2
ON s.StudentID = mod2.StudentID


--We often want to return only rows when there is nothing in a particular column. Say we wanted to see only students who had not completed their modules; 
--we would look for those with an empty Mark column.

SELECT s.FirstName, s.Surname, sm.ModuleID
FROM dbo.StudentModule sm
INNER JOIN dbo.Student s
	 ON sm.StudentID = s.StudentID
WHERE sm.OverallMark = '' -- WHERE sm.OverallMark IS NULL         and can use for not nulls -       WHERE sm.OverallMark IS NOT NULL



--inserting new data:
INSERT INTO dbo.CourseModule
VALUES ('BS', 'CS1004')


--How would we return all Lecturers that were both Module Leaders and Course Tutors? 
SELECT l.StaffID, l.Surname
FROM dbo.Lecturer AS l
INNER JOIN dbo.Module AS m ON l.StaffID = m.ModuleConvenor
	INTERSECT             -- can use UNION ALL or EXCEPT
SELECT l.StaffID, l.Surname
FROM dbo.Lecturer AS l
INNER JOIN dbo.Course As c ON l.StaffID = c.CourseTutorCode



-- Uniting columns (must be the same data type, so convert one data to the other type first using CAST):
SELECT 'Student Fees: £' + CAST(SUM(CourseFees) AS varchar)

--CONVERT() – gives more power when converting Dates, or converting numbers to currency formats

--amending existing rows UPDATE:
UPDATE dbo.Student
SET Email = 'new_email@gmail.com', Town = 'London'
WHERE StudentID = 'S101'

-- deleting rows, always filter:
DELETE FROM dbo.Student
WHERE Town = 'London'


--5.	Show the lowest overall mark that each lecturer has awarded on any of their modules, displaying the Staff ID, the lecturer’s first and last names,
--the Module ID and description and the relevant mark.

SELECT l.staffID, l.FirstName, L.Surname, m.ModuleDescription, m.ModuleID, sm.OverallMark
FROM dbo.Lecturer AS l
join dbo.Module as m
	on l.StaffID = m.ModuleConvenor
JOIN DBO.StudentModule AS sm 
	on m.ModuleID = sm.ModuleID
WHERE  sm.overallmark in (SELECT MIN(sm1.overallmark)
			           FROM dbo.StudentModule AS sm1 where sm.ModuleID = sm1.ModuleID)


--CANT DO THIS ???? 6.	Display the ID, Name and average Exam and Coursework weights for all lecturers and make sure all the columns have suitable headings, using a correlated query. 
--Investigate use of the ISNULL function to produce suitable output in the case of a lecturer not teaching any modules.

SELECT l.staffID, l.FirstName, L.Surname, AVG(m.CWWeight) as 'AverageCWW', avg(m.ExamWeight) as 'AverageEW'
FROM dbo.Lecturer AS l
join dbo.Module as m
	on l.StaffID = m.ModuleConvenor
JOIN DBO.StudentModule AS sm 
	on m.ModuleID = sm.ModuleID
group by l.staffID, l.FirstName, L.Surname


SELECT l.staffID, l.FirstName, L.Surname, AVG(m.CWWeight) as 'AverageCWW', avg(m.ExamWeight) as 'AverageEW'
FROM dbo.Lecturer AS l
join dbo.Module as m
	on l.StaffID = m.ModuleConvenor
JOIN DBO.StudentModule AS sm 
	on m.ModuleID = sm.ModuleID
WHERE  avg(m.cwweight) in (SELECT avg(m1.cwweight)
			           FROM dbo.Module AS m1 where m.ModuleId = m1.ModuleID)



-- 7.	Select all courses that include both modules CS2026 and BS2029, showing their ID and description.

SELECT c.CourseDescription
FROM dbo.Course AS c
JOIN (SELECT c1.CourseCode
      FROM dbo.Course AS c1
      INNER JOIN dbo.CourseModule AS cm
	       ON c1.CourseCode = cm.CourseCode
      WHERE cm.ModuleID = 'cs2026') AS mod1
ON c.CourseCode = mod1.CourseCode
JOIN (SELECT c1.CourseCode
      FROM dbo.Course AS c1
      INNER JOIN dbo.CourseModule AS cm
	       ON c1.CourseCode = cm.CourseCode
      WHERE cm.ModuleID = 'bs2029') AS mod2
ON c.CourseCode = mod2.CourseCode


--8.	Show all the students that have completed both BS and CS courses, displaying their ID’s, names and the date completed. 
--cant underatand this!! Investigate the use of CONVERT to display the date completed in such a way that it only shows the date (UK style).

SELECT s.StudentID, s.Surname, s.FirstName, sc.CourseCode, sc.DateCompleted
FROM dbo.Student AS s
join dbo.StudentCourse as sc
	on s.StudentID = sc.StudentID
JOIN (SELECT s1.StudentID
      FROM dbo.Student AS s1
      INNER JOIN dbo.StudentCourse AS sc
	       ON s1.StudentID = sc.StudentID
      WHERE sc.CourseCode= 'bs') AS mod1
ON s.StudentID = mod1.StudentID
JOIN (SELECT s1.StudentID
      FROM dbo.Student AS s1
      INNER JOIN dbo.StudentCourse AS sc
	       ON s1.StudentID = sc.StudentID
      WHERE sc.CourseCode= 'cs') AS mod2
ON s.StudentID = mod2.StudentID

select * from dbo.StudentCourse

SELECT CONVERT(varchar, getdate(), 1)

UPDATE dbo.StudentCourse
SET DateCompleted = '2010-01-10 00:00:00.000'
WHERE StudentID = '1'

UPDATE dbo.StudentCourse
SET DateCompleted = '2010-01-10 00:00:00.000'
WHERE StudentID = '2'

UPDATE dbo.StudentCourse
SET DateCompleted = '2010-01-10 00:00:00.000'
WHERE StudentID = '3'

UPDATE dbo.StudentCourse
SET DateCompleted = '2010-01-10 00:00:00.000'
WHERE StudentID = '4'



--9a.	unfinished! Write a query to show the IDs and Email addresses of all the Students and Lecturers, 
--with the exception of all the students who are Excluded and those students and lecturers without email addresses.

select s.StudentID, s.Email, l.StaffID, l.Email
from dbo.Student as s
full join dbo.StudentCourse as sc
	on s.StudentID = sc.StudentID
full join dbo.Lecturer as l
	on sc.Tutor = l.StaffID
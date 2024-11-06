-- Script that creates a view that lists
-- all students that have a score

CREATE VIEW need_meeting
	AS SELECT * FROM students
	WHERE score < 80 AND 
		(last_meeting IS NULL 
			OR (YEAR(last_meeting) - YEAR(CURDATE())) > 1);

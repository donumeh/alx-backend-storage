-- Create a stored procedure that adds a
-- new correction for a student


DROP PROCEDURE IF EXISTS AddBonus;

DELIMITER $$ ;

CREATE PROCEDURE AddBonus(
	IN user_id INT, 
	IN project_name VARCHAR(255), 
	IN score INT)
	BEGIN
		DECLARE project_name_avail VARCHAR(255);
		DECLARE new_project_id INT;

		SELECT name INTO project_name_avail FROM projects
		WHERE name = project_name;

		-- SELECT project_name, project_name_avail, "OUTSIDE";

		IF project_name_avail IS NULL THEN

			INSERT INTO projects (name) VALUES
			(project_name);
			SET new_project_id = LAST_INSERT_ID();

			-- SELECT project_name, project_name_avail, "INSIDE 1";

		ELSE
			SELECT id INTO new_project_id FROM projects
			WHERE name = project_name;

			-- SELECT project_name, project_name_avail, "INSIDE 2";
		END IF;

		INSERT INTO corrections (user_id, project_id, score)
		VALUES (user_id, new_project_id, score);
	END $$


DELIMITER ; $$

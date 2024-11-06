-- SQL script that creates a stored procedure
-- to compute and store the average weighted

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;

DELIMITER $$ ;

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	DECLARE sum_weight_avg INT;

	SELECT SUM(weight) INTO sum_weight_avg FROM projects;


	UPDATE users u
	SET u.average_score = (
		SELECT SUM(score * (
			SELECT weight FROM projects
			WHERE corrections.project_id = projects.id
		)) / sum_weight_avg  FROM corrections
		WHERE corrections.user_id = u.id
	);
END $$

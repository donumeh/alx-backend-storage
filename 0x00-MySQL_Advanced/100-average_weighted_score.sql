-- Script that calculates the
-- average weighted score

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;

DELIMITER $$ ;

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
	DECLARE sum_weight INT;
	DECLARE sum_weighted_scores INT;
	DECLARE user_id_input INT;

	SET user_id_input = user_id;

	-- SELECT user_id_input;

	SELECT SUM(weight) INTO sum_weight
	FROM projects;

	-- SELECT sum_weight;

	SELECT SUM(score *
		(SELECT weight FROM projects
		WHERE id = project_id)) INTO sum_weighted_scores
	FROM corrections
	WHERE corrections.user_id = user_id_input;

	UPDATE users
	SET average_score = (sum_weighted_scores / sum_weight)
	WHERE id = user_id;
END $$

DELIMITER ; $$

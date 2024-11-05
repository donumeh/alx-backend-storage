-- Creates trigger that updates valid_email boolean
-- when a new email is set

DELIMITER $$ ;

CREATE TRIGGER update_valid_email_trigger
	BEFORE UPDATE ON users
	FOR EACH ROW
	BEGIN
		IF NEW.email <> OLD.email THEN
			SET NEW.valid_email = 0;
		END IF;
	END $$

DELIMITER ; $$

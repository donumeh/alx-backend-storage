-- Old school band
-- SQL script that lists all brands with `Glam rock` as main style
-- ranked by their longevity

SELECT band_name, IFNULL(split, "2022") - formed as lifespan
	FROM metal_bands
	WHERE style LIKE "%Glam rock%";

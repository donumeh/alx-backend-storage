-- Creates an index idx_name_first on table names

CREATE INDEX IF NOT EXISTS idx_name_first ON names(name(1));

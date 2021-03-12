-- Initialize the database.
-- Drop any existing data and create empty tables.

CREATE TABLE "tracks" (
	"spotify_id"	TEXT NOT NULL UNIQUE,
	"name"	TEXT,
	"artist"	TEXT,
	"features"	TEXT,
	"analysis"	TEXT,
	PRIMARY KEY("spotify_id")
);
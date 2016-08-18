-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

--scrub existing database; create & connect to new database
DROP database tournament;
CREATE database tournament;
\c tournament;

--create table of all players
CREATE TABLE Players (
	player_id serial primary key,
	player_name text
);

--create table for matches, with winner and loser identified
CREATE TABLE Matches (
	match_id serial primary key,
	winner_id serial references Players(player_id),
	loser_id serial references Players(player_id)				
);

-- Creates a view of the standings:
CREATE VIEW Standings AS
SELECT Players.player_id, Players.player_name,
	SUM(CASE WHEN Matches.winner_id = Players.player_id THEN 1 ELSE 0 END) AS wins,
	count(Matches.*) AS matches
FROM Players LEFT JOIN Matches ON Players.player_id = Matches.winner_id OR Players.player_id = Matches.loser_id
GROUP BY Players.player_id;


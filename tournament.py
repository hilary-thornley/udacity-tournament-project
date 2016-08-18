#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2

def connect():
	"""Connect to the PostgreSQL database.  Returns a database connection."""
	return psycopg2.connect("dbname=tournament")

def deleteMatches():
	"""Remove all the match records from the database."""
	dbconnect = connect()
	c = dbconnect.cursor()
	c.execute("DELETE FROM Matches;")
	dbconnect.commit()
	dbconnect.close()


def deletePlayers():
    """Remove all the player records from the database."""
    dbconnect = connect()
    c = dbconnect.cursor()
    c.execute("DELETE FROM Players;")
    dbconnect.commit() 
    dbconnect.close()


def countPlayers():
	"""Returns the number of players currently registered."""
	dbconnect = connect()
	c = dbconnect.cursor()
	c.execute("SELECT COUNT(*) from Players;")
	count = c.fetchone()[0]
	dbconnect.commit() 
	dbconnect.close()
	return count 


def registerPlayer(name):
	"""Adds a player to the tournament database.
	The database assigns a unique serial id number for the player.  (This
	should be handled by your SQL database schema, not in your Python code.)
	
	Args:
	
	name: the player's full name (need not be unique).
	"""
	dbconnect = connect()
	c = dbconnect.cursor()
	c.execute("INSERT INTO Players(player_name) VALUES (%s)",(name,))
	dbconnect.commit() 
	dbconnect.close()


def playerStandings():
	"""Returns a list of the players and their win records, sorted by wins.
	The first entry in the list should be the player in first place, or a player
	tied for first place if there is currently a tie.
	
	Returns:
	
	A list of tuples, each of which contains (id, name, wins, matches):
	
	id: the player's unique id (assigned by the database)
	name: the player's full name (as registered)
	wins: the number of matches the player has won
	matches: the number of matches the player has played
	"""
	dbconnect = connect()
	c = dbconnect.cursor()
	c.execute("SELECT * FROM Standings ORDER BY wins DESC;")
	standings = c.fetchall()
	dbconnect.commit() 
	dbconnect.close()
	return standings


def reportMatch(winner, loser):
	"""Records the outcome of a single match between two players.
	
	Args:
	
	winner:  the id number of the player who won
	loser:  the id number of the player who lost
	"""
	dbconnect = connect()
	c = dbconnect.cursor()
	c.execute("INSERT INTO Matches(winner_id, loser_id) VALUES (%s, %s)", (winner, loser,))
	dbconnect.commit() 
	dbconnect.close()
 
 
def swissPairings():
	"""Returns a list of pairs of players for the next round of a match.
	
	Assuming that there are an even number of players registered, each player
	appears exactly once in the pairings.  Each player is paired with another
	player with an equal or nearly-equal win record, that is, a player adjacent
	to him or her in the standings.
	
	Returns:
	
	A list of tuples, each of which contains (id1, name1, id2, name2)
	
	id1: the first player's unique id
	name1: the first player's name
	id2: the second player's unique id
	name2: the second player's name
	"""
	ranking = playerStandings()
	count = 0
	pairings = []
	while count < len(ranking):
		player1_id = ranking[count][0]
		player1_name = ranking[count][1]
		player2_id = ranking[count+1][0]
		player2_name = ranking[count+1][1]
		pairings.append((player1_id,player1_name, player2_id, player2_name))
		count += 2
	return pairings
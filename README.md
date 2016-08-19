<h1># udacity-tournament-project</h1>
<p>Final project for the Back-end Developer path (Stage 5) of Udacity's "Intro to Programming" Nanodegree</p>

<h2>Start-up Instructions:</h2>
<p>
<ul>
<li>Follow Udacity's guide to installing and running Vagrant: https://www.udacity.com/wiki/ud197/install-vagrant?_ga=1.62732204.1876431276.1456523634</li>
<li>Open GitBash and navigate to the Vagrant directory (i.e. cd fullstack/vagrant/tournament)</li>
<li>Enter vagrant up, then enter vagrant ssh</li>
<li>Navigate to tournament directory (i.e. cd /vagrant/tournament) and enter psql</li>
<li>Enter \i tournament.sql. Confirm following output:<br></li>
<code>
DROP DATABASE
CREATE DATABASE
You are now connected to database "tournament" as user "vagrant".
CREATE TABLE
CREATE TABLE
CREATE VIEW
</code>
<li>Enter \q</li>
<li>Enter python tournament_test.py.  Confirm following output:</li>
<code>
1. countPlayers() returns 0 after initial deletePlayers() execution.
2. countPlayers() returns 1 after one player is registered.
3. countPlayers() returns 2 after two players are registered.
4. countPlayers() returns zero after registered players are deleted.
5. Player records successfully deleted.
6. Newly registered players appear in the standings with no matches.
7. After a match, players have updated standings.
8. After match deletion, player standings are properly reset.
9. Matches are properly deleted.
10. After one match, players with one win are properly paired.
Success!  All tests pass!
</code>
</ul>
</p>

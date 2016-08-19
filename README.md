<h1># udacity-tournament-project</h1>
<p>Final project for the Back-end Developer path (Stage 5) of Udacity's "Intro to Programming" Nanodegree</p>

<h2>Start-up Instructions:</h2>
<p>
<ul>
<li>Follow Udacity's guide to installing and running Vagrant: https://www.udacity.com/wiki/ud197/install-vagrant?_ga=1.62732204.1876431276.1456523634</li>
<li>Open GitBash and navigate to the Vagrant directory (i.e. cd fullstack/vagrant/tournament)</li>
<li>Enter vagrant up, then enter vagrant ssh</li>
<li>Navigate to tournament directory (i.e. cd /vagrant/tournament) and enter psql</li>
<li>Enter \i tournament.sql. Confirm following output:</li>
DROP DATABASE<br>
CREATE DATABASE<br>
You are now connected to database "tournament" as user "vagrant".<br>
CREATE TABLE<br>
CREATE TABLE<br>
CREATE VIEW<br>
<li>Enter \q</li>
<li>Enter python tournament_test.py.  Confirm following output:</li>
1. countPlayers() returns 0 after initial deletePlayers() execution.<br>
2. countPlayers() returns 1 after one player is registered.<br>
3. countPlayers() returns 2 after two players are registered.<br>
4. countPlayers() returns zero after registered players are deleted.<br>
5. Player records successfully deleted.<br>
6. Newly registered players appear in the standings with no matches.<br>
7. After a match, players have updated standings.<br>
8. After match deletion, player standings are properly reset.<br>
9. Matches are properly deleted.<br>
10. After one match, players with one win are properly paired.<br>
Success!  All tests pass!<br>
</ul>
</p>

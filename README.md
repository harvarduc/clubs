# List of Harvard clubs for the UC Finance Committee

## Compiling the list

1. Get a text editor like Atom.
1. Go [here](https://osl.fas.harvard.edu/student-organizations) and copy the list of clubs to `osl-clubs-raw.txt`. No need to clean the data.
1. Go [here](http://recreation.gocrimson.com/recreation/club_sports/active_clubsports) and copy the list of club sports to `club-sports-raw.txt`. The only cleaning you have to do is to make sure all club sports are on one line (e.g. Volleyball tends to spill onto 2 lines).
1. Run `python compile-ficom-list.py`.
1. Your list of clubs eligible for FiCom funding will be in `ficom-clubs.txt`!

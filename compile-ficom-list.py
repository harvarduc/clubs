"""
Compiles a list of all the clubs that the Finance Committee can fund,
given some raw input files.
"""

def main():
    # read the osl clubs and club sports files

    # file paths
    # TODO make this configurable
    osl_clubs_path = "osl-clubs-raw.txt"
    club_sports_path = "club-sports-raw.txt"

    # open files
    with open(osl_clubs_path,"r") as osl_clubs_file, open(club_sports_path,"r") as club_sports_file:
        # read these into lists
        osl_clubs = osl_clubs_file.read().splitlines()
        club_sports_path = club_sports_file.read().splitlines()

        print osl_clubs

if __name__ == "__main__":
    main()

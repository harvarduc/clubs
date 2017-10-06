"""
Compiles a list of all the clubs that the Finance Committee can fund,
given some raw input files.
"""

# temporary debugging variable
output = None

def main():
    global output

    # read the osl clubs and club sports files

    # file paths
    # TODO make this configurable
    osl_clubs_path = "osl-clubs-raw.txt"
    club_sports_path = "club-sports-raw.txt"
    output_path = "ficom-clubs.txt"

    # open files
    with open(osl_clubs_path,"r") as osl_clubs_file, open(club_sports_path,"r") as club_sports_file:
        # read these into lists
        osl_clubs = osl_clubs_file.read().splitlines()
        club_sports = club_sports_file.read().splitlines()

        # clean each list by removing duplicates, trimming spaces, etc
        osl_clubs_cleaned = clean_list(osl_clubs)
        club_sports_cleaned = clean_list(club_sports)

        # ok now merge these
        merged = []
        merged.extend(osl_clubs_cleaned)
        merged.extend(club_sports_cleaned)

        # now that we have the full list, we have some UC-specific things to remove
        # first, remove anything with PBHA
        no_pbha = [s for s in merged if s.find("PBHA") < 0]

        # now remove the UC itself
        no_uc = [s for s in no_pbha if s.find("Undergraduate Council") < 0]

        # sort it before reporting
        # sort case insensitively
        sorted_list = sorted(no_uc, key=lambda s: s.lower())

        # report answer
        output = sorted_list

        # write the list to a file, with one club per line
        with open(output_path, "w") as outfile:
            for line in output:
                # this just means to write the line of text with a newline ("\n") at the end
                outfile.write("{}\n".format(line))

        print "Done!"

def clean_list(raw_list):
    """
    Cleans up a list of raw text by:
        -   Removing blank lines
        -   Trimming extra spaces
        -   Removing duplicates
    """
    # first strip extra spaces
    stripped = [s.strip() for s in raw_list]

    # remove blank lines
    no_empties = [s for s in stripped if s != ""]

    # remove duplicates just to be safe
    no_duplicates = list(set(no_empties))

    return no_duplicates


if __name__ == "__main__":
    main()

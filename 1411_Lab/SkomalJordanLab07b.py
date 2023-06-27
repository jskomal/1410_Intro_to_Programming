# Jordan Skomal | 6/27/23


def get_avg_score():
    score_file = open("score.txt", "r")
    outfile_name = input("Please enter a name for the output file: ")
    outfile = open(outfile_name, "w")
    for line in score_file:
        temp_split = line.split()
        uname = temp_split[0]
        scores = list(map(float, temp_split[1:-1]))
        avg = sum(scores) / len(scores)
        print(f"{uname} {avg}")
        print(f"{uname} {avg}", file=outfile)

    score_file.close()


get_avg_score()

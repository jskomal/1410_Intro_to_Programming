def batch_names():
    infile = open("names.txt", "r")
    outfile = open("out.txt", "w")
    for line in infile:
        fname, lname = line.split(" ")
        print(f"{fname[0]}{lname[:-1]}", file=outfile)


batch_names()

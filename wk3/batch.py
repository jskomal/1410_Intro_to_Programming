from tkinter.filedialog import asksaveasfilename


def main():
    infile = open("names.txt", "r")
    outfile = asksaveasfilename()

    for line in infile:
        first, last = line[:-1].split(" ")
        uname = f"{first[0].casefold()}{last[:4].casefold()}"
        print(uname, file=outfile)

    infile.close()
    outfile.close()


main()

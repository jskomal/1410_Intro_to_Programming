# read_data
# reads a set of numbers from an input file
# params: file_name:string
# returns a number[]

from math import sqrt


def read_data(file_name: str):
    file = open(file_name, "r")
    result = []
    for line in file:
        result.append(int(line))
    return result


def compute_sum(int_list):
    acc = 0
    for num in int_list:
        acc += num
    return acc


def compute_mean(int_list):
    acc = 0
    for num in int_list:
        acc += num
    return acc / len(int_list)


def compute_sd(int_list):
    mean = compute_mean(int_list)
    acc = 0
    for num in int_list:
        deviation = num - mean
        deviation *= deviation
        acc += deviation
    size = len(int_list)
    result = sqrt(acc / (size - 1))
    return result


def write_result(output_filename, int_sum, mean, sd):
    outfile = open(output_filename, "w")
    print(f"Sum is: {int_sum}", file=outfile)
    print(f"Mean is: {mean}", file=outfile)
    print(f"Standard Deviation is: {sd:.2f}", file=outfile)
    outfile.close()


def main():
    infile_name = input("Please enter the input filename: ")
    outfile_name = input("Please enter the output filename: ")
    my_list = read_data(infile_name)
    my_sum = compute_sum(my_list)
    my_mean = compute_mean(my_list)
    my_sd = compute_sd(my_list)
    write_result(outfile_name, my_sum, my_mean, my_sd)


main()

import os
import timeit

FILE_SIZE = 50 * 1048576

def generate_file(filename):
    num = 0
    with open(filename, 'w') as f:
        while os.path.getsize(filename) <= FILE_SIZE:
            f.write(str(num) + '\n')
            num += 1




def main():
    filename = "50mb.txt"
    # generate_file(filename)
    s = """
num = 0
with open('50mb.txt', 'r') as f:
    lines = f.readlines()

for line in lines:
    if line.strip().isdigit():
        num += int(line.strip())
    """
    print(timeit.timeit(s, number=10))


    s = """
num = 0
with open('50mb.txt', 'r') as f:
    for line in f:
        if line.strip().isdigit():
            num += int(line.strip())
    """

    print(timeit.timeit(s, number=10))

    s = """
file_sum = 0
with open('50mb.txt', 'r') as f:
   num = (int(line.strip()) for line in f if line.strip().isdigit())
   file_sum = sum(num)
    """

    print(timeit.timeit(s, number=10))


if __name__ == "__main__":
    main()

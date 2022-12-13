import csv
def main():
    """ EXERCISE 1.6 """
    
    userInput = input("Enter file name: ")
    with open(userInput, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        with open('user_results.csv', 'w', newline='') as new_file:
            csv_writer = csv.writer(new_file)
            for line in csv_reader:
                if line == ['n', 'a_n', 'b_n', 'c_n', 'avg']:
                    csv_writer.writerow(line)
                else:
                    a_n, b_n, c_n = float(line[1]), float(line[2]), float(line[3])
                    if a_n > 0 and b_n > 0 and c_n > 0:
                        csv_writer.writerow(line)



if __name__ == '__main__':
    main()
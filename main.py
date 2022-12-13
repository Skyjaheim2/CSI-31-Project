import numpy as np
import csv

def main():
    """ EXERCISE 1.3, 1.4, 1.5 """

    testValues = {
        1: {'a':2, 'b': 2, 'c': 3, 'alpha': -1, 'beta': 1},
        2: {'a': 2, 'b': 2, 'c': 3, 'alpha': 2.5, 'beta': -1},
        3: {'a': 2, 'b': 2, 'c': 3, 'alpha': -1, 'beta': 3},
        4: {'a': 2, 'b': 2, 'c': 3, 'alpha': 7, 'beta': -3},
    }

    for i in range(1,5):
        a = testValues[i]['a']
        b = testValues[i]['b']
        c = testValues[i]['c']

        alpha = testValues[i]['alpha']
        beta = testValues[i]['beta']

        print(f"When a={a}, b={b}, c={c}, and alpha={alpha}, beta={beta}")

        A = np.matrix([[alpha, beta, beta],
                       [beta, alpha, beta],
                       [beta, beta, alpha]])

        X0 = np.array([
            [a],
            [b],
            [c]
        ])
        with open(f'results_{i}.csv', 'w', newline='') as new_file:


            csv_writer = csv.writer(new_file)
            csv_writer.writerow(['n', 'a_n', 'b_n', 'c_n', 'avg'])
            for n in range(1, 21):
                Xn = (A**n)*X0
                a_n = Xn[0].A[0][0]
                b_n = Xn[1].A[0][0]
                c_n = Xn[2].A[0][0]
                avg = round((a_n+b_n+c_n)/3, 5)
                print(f"{n},{a_n},{b_n},{c_n}")
                csv_writer.writerow([n, a_n, b_n, c_n, avg])

            print()






main()
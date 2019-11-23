class HappyNums:

    def __init__(self):
        my_num = int(input("Enter a num: "))
        self.print_happy(my_num)

    def sum_squares_digits(self, n):
        sum_sq = 0

        for d in str(n):
            sum_sq += (int(d) * int(d))

        return sum_sq

    def check_happy(self, n):
        n1 = n
        while n1 != 4 and n1 != 1:
            n1 = self.sum_squares_digits(n1)

            if n1 == 1:
                print(n1, "is happy")
            else:
                print(n1, "is not happy")

    def print_happy(self, n):
        print("All happy numbers up to ", n, "are: ")
        n1 = n + 1
        for i in range(1, n1):
            self.check_happy(i)



hn = HappyNums()
print(hn.check_happy(19))
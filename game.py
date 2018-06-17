import random

class My_Secret_number:
    def __init__(self):
        self.__trials = 0
        self.__secret = 0

    def New_Game(self,boundary):
        self.__boundary = boundary
        self.__secret = random.randint(1,boundary) # 1부터 boundary 까지의 범위에서 난수 생성
        self.__trials = 0

    def Guess(self,userguess):
        self.__trials += 1

        userguess = int(userguess)

        if userguess > self.__boundary or userguess == 0:
            return "You must enter a number below {}.".format(boundary)

        return userguess - self.__secret

    def Get_Trials(self):
        return self.__trials

if __name__ =='__main__':
    s = My_Secret_number()
    a = s.New_Game(100)

    while True:
        input_number = input("your guess : ")

        result = s.Guess(input_number)
        if result == 0:
            break
        elif result < 0 :
            print("greater")
        elif result > 0 :
            print("smaller")
        else:
            print(result)

    print("SUCCESS in {} tries".format(s.Get_Trials()))

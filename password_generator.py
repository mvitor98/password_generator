import string
import argparse
from random import choice, shuffle
from itertools import combinations_with_replacement
from statistics import stdev
import sys

parser = argparse.ArgumentParser(description="")
parser.add_argument("-l", "--lower", type = int, default = 0, help="Lower case chars a-z")
parser.add_argument("-u", "--upper", type = int, default = 0, help="Upper case chars")
parser.add_argument("-d", "--digits", type = int, default = 0, help="Digits from 0-9")
parser.add_argument("-e", "--extraChars", type = int, default = 0, help="Extra chars and simbols")
parser.add_argument("-r", "--random", action="store_true", 
                    help="Select a random chars generator (must infor a number with -n flag)")
parser.add_argument("-n", "--num", type= int, default= 0, help="Inform how many chars your password should have.")
args = parser.parse_args()


class passwordGeneretor:

    def __init__(self) -> None:
        self.__lower = string.ascii_lowercase
        self.__upper = string.ascii_uppercase
        self.__digits = string.digits
        self.__extra_chars = "!@#4%&*()_+=-<>[]{}?/|"
        self.__num_chars = args.num
        self.password = self.__build_password()

    def __chose_chars(self, charnum: int, charset: list):
        string = ""
        for _ in range(charnum):
            string += choice(charset)
        return string

    def __shuffle_string(self, string):
        string = list(string)
        shuffle(string)
        return "".join(string)

    def __build_password(self) -> str:
        if args.random:
            chars_set = self.__ramdon_generated_chars()
        else:
            chars_set = self.__password_args()
        l, u, d, e = chars_set    
        password = ""
        password += self.__chose_chars(l, self.__lower)
        password += self.__chose_chars(u, self.__upper)
        password += self.__chose_chars(d, self.__digits)
        password += self.__chose_chars(e, self.__extra_chars)
        
        print(f"{l=}, {u=}, {d=}, {e=}")
        return self.__shuffle_string(password)
    
    def __password_args(self):
        return (args.lower, args.upper, args.digits, args.extraChars)

    def __ramdon_generated_chars(self):
        combinations = [i for i in combinations_with_replacement(range(1, self.__num_chars + 1), 4) 
                if sum(i) == self.__num_chars and 1.5 <= stdev(i) <= 3.2]
        return choice(combinations)
    

if __name__ == "__main__": 
    
    owner = input('Inform an owner for the password:\n-> ').lower()

    with open('generated_passwords.txt', 'a+', encoding="utf-8") as file:
        password = passwordGeneretor().password
        file.writelines(f"{owner}: {password}\n")

    print(password)
    
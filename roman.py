

class Solution:
    def romanToInt(self, s: str) -> int:
        number = 0
        roman_to_num = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000

        }
        i = 0
        while(i < len(s)):
            if(s[i] == "I" and i < len(s)-1 and s[i+1] == "V"):

                number += roman_to_num["V"]-roman_to_num["I"]
                # return number
                i = i+1

            elif(s[i] == "I" and i < len(s)-1 and s[i+1] == "X"):
                number += roman_to_num["X"]-roman_to_num["I"]
                # return number
                i = i+1

            elif(s[i] == "X" and i < len(s)-1 and s[i+1] == "L"):
                number += roman_to_num["L"]-roman_to_num["X"]
                # return number
                i = i+1
            elif(s[i] == "X" and i < len(s)-1 and s[i+1] == "C"):
                number += roman_to_num["C"]-roman_to_num["X"]
                # return number
                i = i+1
            elif(s[i] == "C" and i < len(s)-1 and s[i+1] == "D"):
                number += roman_to_num["D"]-roman_to_num["C"]
                # return number
                i = i+1
            elif(s[i] == "C" and i < len(s)-1 and s[i+1] == "M"):
                number += roman_to_num["M"]-roman_to_num["C"]
                # return number
                i = i+1
            else:
                number += roman_to_num[s[i]]
            i = i+1

        return number

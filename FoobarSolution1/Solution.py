def solution(s):
    braille_chars = "000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110"
    letter_chars = "The quick brown fox jumps over the lazy dog"
    letter_no_space = letter_chars.replace(" ", "")
    spliced_braille = []
    letter_to_braille_dict = {}
    ans = ""

    letter_to_braille_dict["upper"] = "000001"
    letter_to_braille_dict[" "] = "000000"

    for index in range(0,len(braille_chars),6):
        if braille_chars[index:index+6] == "000000" or braille_chars[index:index+6] == "000001":
            continue
        else:
            spliced_braille.append(braille_chars[index: index + 6])

    for index in range(len(letter_no_space)):
        letter_to_braille_dict[letter_no_space[index].lower()] = spliced_braille[index]

    for letter in s:
        if letter.isupper():
            ans += letter_to_braille_dict["upper"]
        try:
            ans += letter_to_braille_dict[letter.lower()]
        except:
            print("letter {} not found".format(letter))
    return ans
def test_solution(method_ans, right_ans):
    if right_ans == method_ans:
        return "your braille system works!"
    else:
        return "your braille system does not work :("

tester_dict = {"code":"100100101010100110100010","Braille":"000001110000111010100000010100111000111000100010","The quick brown fox jumps over the lazy dog":"000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110"}
for test in tester_dict:
    print("for the text {}.... ".format(test) + test_solution(solution(test), tester_dict[test]))




#.read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one", "r").read()
email_two = open("email_two", "r").read()
email_three = open("email_three", "r").read()
email_four = open("email_four", "r").read()

#other variables
proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

#methods
def censor(phrase, text, replacement = None):
  if replacement == None:
    replacement = ""
    for letter in phrase:
      replacement += "*"
  return text.replace(" " + phrase + " ", " " + replacement + " ")

def censor_one_list(phrases, text, replacements = []):
  if replacements == []:
    replacements = ["*" for phrase in phrases]
  for phrase in range(len(phrases)):
    text = censor(phrases[phrase], text, replacements[phrase])
  return text

def censor_multiple_lists(unwanted_groups, text, replacement_groups = [], censor_before_and_after = False):
  if replacement_groups == []:
    for group in unwanted_groups:
      replacement_groups.append([])

  if censor_before_and_after:
    for group in range(len(unwanted_groups)):
      ind = text.index(unwanted_groups[group]) - 1
      while unwanted_groups[group] in text and ind >= 2:
        ind = text.index(unwanted_groups[group]) - 2
        word = ""
        while text[ind] != " " and ind >= 0:
          word += text[ind]
          ind -= 1
        word = word[-1:0]
        print(word)
        print("Desired test: " + text[ind + len(unwanted_groups[group]): ind + len(unwanted_groups[group]) + len(word)])
        if text[ind + len(unwanted_groups[group]) : ind + len(unwanted_groups[group]) + len(word)] == word:
          text = censor(word, text)
      text = censor_one_list(unwanted_groups[group], text, replacement_groups[group])
      return text

  else:
    for group in range(len(unwanted_groups)):
      text = censor_one_list(unwanted_groups[group], text, replacement_groups[group])
    return text

#def censor_before_and_after(unwanted_groups, text, replacement_groups = []):

#testers
'''
print("***************Tester for censor()***********************\n" + censor("learning algorithms", email_one) + "\n")
print("***************Tester for censor()_one_list***********************\n" + censor_one_list(proprietary_terms, email_two) + "\n")
print("***************Tester for censor()_multiple_lists***********************\n" + censor_multiple_lists([proprietary_terms, negative_words], email_two) + "\n")
'''
print("***************Tester for censor()_multiple_lists***********************\n" + censor_multiple_lists(unwanted_groups = ["good"], text = "I are good are", replacement_groups = [], censor_before_and_after = True) + "\n")
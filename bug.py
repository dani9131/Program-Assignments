print("Welcome to the addition helper")
number1 = input("Please enter the first number:" )
number2 = input("Please enter the second number:")

print("The result is:", number1 + number2)

greeting = 1

# 1
if greeting in ["Arrr!"]:
    print("Go away, pirate.")
else: 
        print("Greetings, hater of pirates!")
                
# 2
authors = {
    "Charles Dickens": "1870",
    "William Thackeray": "1863",
    "Anthony Trollope": "1882",
    "Gerard Manley Hopkins": "1889"
}

for author, date in authors.items():
    print ("%s" % author + "died in"  + "%s." % date)

                
# 3
year = int(input("Greetings! What is your year of origin?"))

if year < 2021:
    print ("Woah, that's the past!")
elif year == 2021:
    print ("That's totally the present!")
else:
    print ("Far out, that's the future!!")
           
           
# 4
class Person:
  def __init_(self, first_name, last_name):
    self.first = first_name
    self.last = last_name
  def speak(self):
    print("My name is "+ self.first+ " " + self.last)

me = Person("Brandon", "Walsh")
you = Person("Ethan", "Reed")

me.speak()
you.speak
           
# 5
exam_one = int(input("Input exam grade one: "))

exam_two = input("Input exam grade two: ")

exam_3 = str(input("Input exam grade three: "))

grades = [exam_one, exam_two, exam_three]
sum = 0
for grade in grade:
  sum = sum + grade

avg = sum / len(grdes)

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90:
    letter_grade = "B"
elif avg > 69 and avg < 80:
    letter_grade = "C"
elif avg <= 69 and avg >= 65:
    letter_grade = "D"
else:
    letter_grade = "F"

for grade in grades:
    print("Exam: " + str(grade))

    print("Average: " + str(avg))

    print("Grade: " + letter_grade)

if letter_grade =="F":
    print ("Student is failing.")
else:
    print ("Student is passing.")
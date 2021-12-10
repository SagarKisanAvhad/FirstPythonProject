# elif means agar if wali condition fail ho gayi toh koyi baat nhi
# ye condition check kr lo
age = 10
if age >= 18:
    print("You are an adult")
    print("You can vote")
elif age < 18 and age >3:
    print("you are in school")
else:
    print("you are not adult")
    print("you can not vote")

print("Thank you")
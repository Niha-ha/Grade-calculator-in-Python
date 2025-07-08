score = float(input("Enter the score:"))   
#took float input so that we can take both float and integer score


if 0 > score or 100 < score:
    print("Invalid score!!")
elif score < 40:
    print("The Grade is F or fail")
elif score < 50:
    print("The Grade is E-")
elif score < 60:
    print("The Grade is E")
elif score < 70:
    print("The Grade is D")
elif score < 80:
    print("The Grade is C")
elif score < 90:
    print("The Grade is B")
else:
    # score <= 100:
    print("The Grade is A")


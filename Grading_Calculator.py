score_input = input("Enter score: ")
course_type = input("Enter course type (d/n): ")

try:
    score = float(score_input)

    if score < 0 or score > 100:
        print("The score must be in the range of 0 to 100.")

    elif course_type not in ("d", "n"):
        print("The course type is not recognised.")

    elif course_type == "n":
        if score >= 51:
            print("PASSED")
        else:
            print("FAILED")

    elif course_type == "d":
        if score < 51:
            print("F")
        elif score <= 60:
            print("E")
        elif score <= 70:
            print("D")
        elif score <= 80:
            print("C")
        elif score <= 90:
            print("B")
        else:
            print("A")

except ValueError:
    print("The score must be a number.")
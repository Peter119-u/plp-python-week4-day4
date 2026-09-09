score = int(input("Enter your score (0-100): "))

# Check if the score is outside the valid range
if score < 0 or score > 100:
    print("Error: Score must be between 0 and 100.")
else:
    # Check if the score is 80 or higher
    if score >= 80:
        grade = "A"
    # Check if the score is 70 to 79
    elif score >= 70:
        grade = "B"
    # Check if the score is 60 to 69
    elif score >= 60:
        grade = "C"
    # Check if the score is 50 to 59
    elif score >= 50:
        grade = "D"
    # Any remaining valid score is an F
    else:
        grade = "F"

    print(f"A score of {score} earns grade: {grade}")

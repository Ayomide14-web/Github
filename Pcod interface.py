# Function to check PCOS(Polycystic ovary syndrome) 
print("Welcome to the PCOS Prediction System!")

# User input
weight= float(input("Enter your weight(Kg): "))
diet_milk_product=int(input("Rank your Milk Product consumption (1-7): "))
diet_vegetable=int(input("Rank your Vegetable consumption (1-7): "))
diet_fruit=int(input("Rank your Fruit consumption (1-7): "))                 
diet_fat=int(input("Rank your Fat consumption (1-7): "))   
diet_fried_food =int(input("Rank your Fat consumption (1-7): "))
exercise= input("How often do you exercise? (rarely, daily, 1-2 times a week, 3-4 times a week): ").strip().lower()
smoking= input("Do you smoke? (Yes/No): ").strip().lower()
stress_level=input("Do you experience Stress frequently? (Yes/No): ").strip().lower()
menstrual_irregularity=input("Do you go through Menstrual Irregularity? (Yes/No): ").strip().lower()

# Simple encoding
exercise_encoded={"rarely":0, "daily":3, "1-2 times a week":1, "3-4 times a week":2}.get(exercise,0)
stress_encoded=1 if stress_level=="yes" else 0
smoking_encoded=1 if smoking=="yes" else 0
menstrual_encoded=1 if menstrual_irregularity=="yes" else 0

# Manual prediction logic(replace with ML model if needed)
risk_score=weight*0.1+diet_fried_food+diet_fat-diet_vegetable-diet_fruit-exercise_encoded+stress_encoded+menstrual_encoded

#THreshold for High-Risk PCOS (This is an example; you can adjust based on data)
if risk_score>10: 
     print("Prediction: High Risk of PCOS")
     print("Suggested Advice: ")
     print("Reduce Fried and Fatty foods")
     print("Increase intake of fresh vegetable and fruits")
     print("Engage in regular exercise(at least 3-4 times a week.")
     print("Reduce Stress through yoga, meditation or therapy.")
     print("Consult a gynecologist for personalize medical advice.")
else:
    print("Prediction: Low Risk PCOS")
    print("Keep maintaining a healthy lifestyle")

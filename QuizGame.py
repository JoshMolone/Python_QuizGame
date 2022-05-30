


print("Hello World"); 

playing = input("Do you want to play? ");

if playing != "yes":
    quit()

print("Excellent Choice. Let's begin");
print("--------------------------");

score = 0; 

answer = input("QUESTION 22: ")
if answer.upper() == "ANSWER":
        print("Correct Answer")
        score +=1 
else:
    print("Incorrect Answer")

answer = input("QUESTION 2: ")
if answer.upper() == "ANSWER":
        print("Correct Answer")
        score +=1 
else:
    print("Incorrect Answer")

answer = input("QUESTION 3: ")
if answer.upper() == "ANSWER":
        print("Correct Answer")
        score +=1 
else:
    print("Incorrect Answer")

answer = input("QUESTION 4: ")
if answer.upper() == "ANSWER":
        print("Correct Answer") 
        score +=1 
else:
    print("Incorrect Answer")

answer = input("QUESTION 5: ")
if answer.upper() == "ANSWER":
        print("Correct Answer")
        score +=1 
else:
    print("Incorrect Answer")


print("Your score " + str(score))

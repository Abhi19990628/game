questions=[
    ["which language was used to creat fb?",
           "python","java","php","french","none",4],
    
    ["which language was used to creat fb?",
           "python","java","php","french","none",4],
    
    ["which language was used to creat fb?",
           "python","java","php","french","none",4],
    
    ["which language was used to creat fb?",
           "python","java","php","french","none",4],
    
    ["which language was used to creat fb?",
           "python","java","php","french","none",4],
    
    ["which language was used to creat fb?",
           "python","java","php","french","none",4],
    
    ["which language was used to creat fb?",
           "python","java","php","french","none",4],
    
    ["which language was used to creat fb?",
           "python","java","php","french","none",4], 
    
    ["which language was used to creat fb?",
           "python","java","php","french","none",4], 
    
     ["which language was used to creat fb?",
           "python","java","php","french","none",4], 
    ]
levels=[1000, 2000, 4000, 8000, 16000, 32000, 64000, 124000, 248000, 496000 ,928000]

money = 0

for i in range (0, len(questions)):
    
    question=questions[i]
    
print(f"Questios for Rs. {levels[i]}")
print(f"a. {question[1]}              b. {question[2]}" )
print(f"c. {question[3]}              d. {question[4]}" )
reply=int(input("Enter your answer(1-4)"))
if (reply==question[-1]):
    print("correct answer you have won Rs.{levels[i]}")
    if (i == 4):
        money =10000
    elif(i == 9):
        money= 248000
        
else:
    print("baggh ja chutiye yha se!")
    breakpoint
        
        
    

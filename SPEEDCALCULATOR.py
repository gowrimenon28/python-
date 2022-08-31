import time
String='hello my world'
wordcount=len(String.split())
print(String)
while True:
    t0=time.time()
    inputtext=str(input('enter the sentence:'))
    t1=time.time()
    accuracy=len(set(inputtext.split())&set(String.split()))
    accuracy=accuracy/wordcount
    timetaken=t1-t0
    wpm=wordcount/timetaken
    print("WPM",wpm,"Accuracy",accuracy,"Timetaken",timetaken)

#Write a loop that never ends, and run it. (To end the loop, press ctrl-C or close the window displaying the output.)
while True:
    marks = input("How many marks did you get? ")
    
    marks = int(marks)
    if marks < 30:
        print("fail")
    elif marks < 50:
        print("just pass") 
    else:
        print("pass")


        
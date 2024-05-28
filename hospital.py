issue=[] 
appointment=0
print("welcome to goodhealth hospital\n health demand couped by sufficient medical supply :)")
while appointment<4:
    choice=int(input("what services would u like to be assisted with ?:\n 1.checkin\n 2.xray\n 3.injection\n 4.checkup\n"))
    if choice ==1:
        chekin=int(input("welcome to our offices!!\n what following issue are u expriencing\n 1.eye problem\n 2.teeth problem"))
        if chekin==1:
            print("please visit DR. saghet fo checkup!")
            issue.append("eye checkup at DR.saghet\n")
        elif chekin==2:
            print("please visit dentist korir for checkup!")
            issue.append("dental checkup at DR.korir")
            break
        else:
            print("choice is not available")
            
    elif choice ==2:
        print("please visit DR.terry for an xray scan!")
        issue.append("xray scan with DR.terry")
    elif choice ==3:
        inject=int(input("where would u like to be injected\n 1.arm\n 2.ass"))
        if inject==1:
            print("plz visit DR. alex for an injection at the arm")
            issue.append("arm injection with DR.alex")
        elif inject==2:
            print("plz visit DR. sandra for an injection at the ass")
            issue.append("ass injection with DR.sandra")
        else:
            print("choice is not available")
            break
    elif choice ==4:
        print("please DR.kitur for general checkup")   
        issue.append("checkup with DR.kitur") 
    else:
        print("choice is not in the list")
        break    
    appointment=appointment+1    
print(issue)       
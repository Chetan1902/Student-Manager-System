print('-'*100)
print("Student Management System".center(80))
print('-'*100)
db={101:{"name":"chetan","city":"nashik","course":"python","per":89}}
while True:
    print("""
                Dashboard
        1.Add student Details
        2.Display Student Details
        3.Update Student Details
        4.Delete Student Details
        5.Filter
        6.break
        """)
    ch=int(input("enter your choice: "))
    if ch==1:
        reg=eval(input("enter the reg.no: "))
        name=input("enter the name: ")
        city=input("enter the city name:")
        per=eval(input("enter the percentage: "))
        course=input("enter course name:")
        db[reg]={"name":name,"city":city,"per":per,"course":course}
        print("Added Successfuly...")
    elif ch==2:
        print('-'*105)
        print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format("reg","name","city","course","per"))
        print('-'*105)
        for i in db:
            print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format(i,db[i]["name"],db[i]["city"],db[i]["course"],db[i]["per"]))
            print('-'*105)
    elif ch==3:
        reg=eval(input("enter the reg no you wnt to update it:"))
        print("""
            1.name
            2.city
            3.per
            4.course
            """)
        ch=eval(input("enter the your choice for update: "))
        if ch==1:
            uname=input("enter the name: ")
            db[reg]["name"]=uname
            print("Updated successfully..")
        elif ch==2:
            ucity=input("enter the city: ")
            db[reg]["city"]=ucity
            print("Updated successfully..")
        elif ch==3:
            uper=eval(input("enter the per: "))
            db[reg]["per"]=uper
            print("Updated successfully..")
        elif ch==4:
            ucourse=input("enter the course name:")
            db[reg]["course"]=ucourse
            print("Updated successfully..")
        else:
            print("invalid choice..")
    elif ch==4:
        reg=eval(input("enter the reg_no:"))
        del db[reg]
        print("Deleted successfully..")
    elif ch==5:
        print("""
            1.By Name
            2.By City
            3.By Course
            """)
        ch=eval(input("enter your choice:"))
        if ch==1:
            name=input("enter name: ")
            print('-'*105)
            print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format("reg","name","city","course","per"))
            print('-'*105)
            for i in db:
                if db[i]["name"]==name:
                    print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format(i,db[i]["name"],db[i]["city"],db[i]["course"],db[i]["per"]))
                    print('-'*105)
        elif ch==2:
                city=input("enter city name: ")
                print('-'*105)
                print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format("reg","name","city","course","per"))
                print('-'*105)
                for i in db:
                    if db[i]["city"]==city:
                        print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format(i,db[i]["name"],db[i]["city"],db[i]["course"],db[i]["per"]))
                        print('-'*105)
        elif ch==3:
                course=input("enter course name: ")
                print('-'*105)
                print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format("reg","name","city","course","per"))
                print('-'*105)
                for i in db:
                    if db[i]["course"]==course:
                        print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format(i,db[i]["name"],db[i]["city"],db[i]["course"],db[i]["per"]))
                        print('-'*105)
        else:
            print("Invalid choice...")
    elif ch==6:
        break
    else:
        print("Invalid Choice...")
        
    """Create project
    1.Employee MS
    2.ATM 
    """
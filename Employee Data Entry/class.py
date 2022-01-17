
class Employee :

    def __init__(__self__,name,designation,salary) :
        print("************************Initilizing values and creating object*******************************")
        print("******************************Employee's Data Has Added**************************************")
        __self__.name= name
        __self__.designation = designation
        __self__.salary= salary

    def getname(__self__) :
        return __self__.name
    
        #print(f"Employee Name is : = {__self__.name}   ")

    def getdesignation(__self__) :
        return __self__.designation

        #print(f"Employee designation : = {__self__.designation}   ")

    def getsalary(__self__) :
        return __self__.salary

        #print(f"Employee salary is : = {__self__.salary}   ")

emplist = []
while True :
    choice = input("Do you want to add employee data.......(y/n)")
    if choice=='y' :
        name_ = input("Enter the name of the employee   ")
        des = input("Enter the designation of the employee   ")
        sal = int(input("Enter the salary of the employee   "))

        emp=Employee(name_,des,sal)
        emplist.append(emp)
    elif choice =='p' :
        for data in emplist :
            print()
            print(f"Employee name is : = {data.getname()} ")
            print(f"Employee designation is : =  {data.getdesignation()} ")
            print(f"Employee salary is : = {data.getsalary()} ")        
            print()
    else :
        break

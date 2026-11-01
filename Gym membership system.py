members_list = []

name = input()
age = int(input())
fee = 500000
positive_answer = "yes"


if age >= 18 :

    is_student = input("is he/she a student? (yes/no) ") == positive_answer
    is_oldmember = input("is he/she an oldmember? (yes/no) ") == positive_answer
    
    if is_student and is_oldmember :
        takhfif_both = fee * 0.3
        fee = fee - takhfif_both 

    elif is_student :
        takhfif_d = fee * 0.2
        fee = fee - takhfif_d

    elif is_oldmember :
        takhfif_o = fee * 0.1
        fee = fee - takhfif_o

    member = {'name':name, 'age': age ,'price' : fee }

    members_list.append(member)
    print (members_list)

else: 
        print("not old enogh")

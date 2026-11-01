members_list = []

positive_answer = "yes"
continue_program = "yes"

while continue_program == "yes":

    name = input("Name: ")
    age = int(input("Age: "))
    fee = 500000

    if age >= 18:

        is_student = input("Is student? (yes/no) ") == positive_answer
        is_oldmember = input("Is oldmember? (yes/no) ") == positive_answer

        if is_student and is_oldmember:
            takhfif_both = fee * 0.3
            fee = fee - takhfif_both

        elif is_student:
            takhfif_d = fee * 0.2
            fee = fee - takhfif_d

        elif is_oldmember:
            takhfif_o = fee * 0.1
            fee = fee - takhfif_o

        member = {'name': name, 'age': age, 'price': fee}

        members_list.append(member)

        print("Member registered successfully!")
        print(member)

    else:
        print("Not old enough!")

    continue_program = input("Add another member? (yes/no) ")

print("\nAll registered members:")
print(members_list)

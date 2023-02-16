# calculae the student
def student_check():
    total_students = int(input("How many stundents to calculate:"))
    math_students = int(input("Number of students with mathematics:"))
    bio_students = int(input("Number of Students with Bio:"))

    no_math_no_bio = total_students-(math_students + bio_students)
    math_and_bio = math_students+bio_students
    # print the results10
    print("Number of stundents without math and bio:", no_math_no_bio)
    print("Number of stundents with math and bio:", math_and_bio)


student_check()

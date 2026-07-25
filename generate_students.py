import random

first_names = [
    "Aarav","Aditi","Rahul","Priya","Arjun","Sneha","Rohan","Ananya",
    "Karthik","Meera","Vivek","Neha","Nikhil","Pooja","Aditya","Diya",
    "Krishna","Harsh","Devika","Akash","Anjali","Varun","Bhavana",
    "Riya","Ishita","Sanjay","Kiran","Nandana","Abhishek","Shreya",
    "Sreya","Anand","Lakshmi","Akhil","Athira","Gokul","Keerthana",
    "Aiswarya","Aravind","Naveen","Manu","Fathima","Nihal","Amal",
    "Sreelakshmi","Aswin","Jithin","Adil","Haseeb","Maya"
]

last_names = [
    "Sharma","Nair","Menon","Reddy","Patel","Gupta","Verma","Singh",
    "Kumar","Das","Pillai","Joseph","Thomas","Mathew","George",
    "Bhat","Yadav","Chopra","Kapoor","Malhotra","Roy","Paul",
    "Iyer","Chandra","Khan","Ali","Hassan","Fernandes",
    "Varghese","Narayanan","Krishnan","Nambiar","Rajan"
]

departments = ["CSE","ECE","EEE","ME","Civil","IT"]

cities = [
    "Kollam","Kochi","Trivandrum","Thrissur",
    "Kozhikode","Kannur","Palakkad",
    "Kottayam","Alappuzha","Malappuram"
]

with open("database/sample_students.sql", "w") as f:

    f.write("TRUNCATE TABLE students RESTART IDENTITY;\n\n")

    for i in range(1,1001):

        first = random.choice(first_names)
        last = random.choice(last_names)

        name = f"{first} {last}"

        dept = random.choice(departments)

        cgpa = round(random.uniform(6.0,10.0),2)

        year = random.randint(1,4)

        city = random.choice(cities)

        email = first.lower()+str(i)+"@tkmce.ac.in"

        f.write(
            f"INSERT INTO students "
            f"(name,department,cgpa,year,city,email) VALUES "
            f"('{name}','{dept}',{cgpa},{year},'{city}','{email}');\n"
        )

print("Generated database/sample_students.sql")

student = {"anil":90,"ravi":80,"amit":70,"anshul":60}
name = input("enter student name: ").strip()

if name in student:
    print(f"{name}'s marks: {student[name]}")
else:
    print(f"student name {name}  is not found in the records")


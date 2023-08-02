def main():
    resume_data = {}
    # 1. Take input from user
    resume_data['Name'] = input("Enter your name: ").upper()
    resume_data['Age'] = int(input("Enter your age: "))
    resume_data['Income'] = float(input("Enter your income: "))
    resume_data['Hobbies'] = input("Enter your hobbies separated by commas: ").split(',')
    resume_data['Father Business'] = input("Enter your father's business: ")
    resume_data['Business Address'] = input("Enter the business address: ")

    siblings_count = int(input("Enter the number of siblings: "))
    siblings = []
    for i in range(siblings_count):
        sibling_name = input(f"Enter the name of sibling {i + 1}: ")
        while True:
          
                sibling_age = int(input(f"Enter the age of sibling {i + 1}: "))
                break
        

        siblings.append({'name': sibling_name, 'age': sibling_age})

    resume_data['Siblings'] = siblings

    # 2. Add educational details
    educational_details = []
    educational_levels = ['School', 'College', 'University']
    for level in educational_levels:
        school_name = input(f"Enter {level} name: ")
        degree = input(f"Enter your degree at {level}: ")
        years = input(f"Enter years attended at {level}: ")
        while True:
            
                passing_marks = int(input(f"Enter your passing marks at {level}: "))
                total_marks = int(input(f"Enter your total marks at {level}: "))
                break
            

        educational_details.append({
            'Level': level,
            'School Name': school_name,
            'Degree': degree,
            'Years': years,
            'Passing Marks': passing_marks,
            'Total Marks': total_marks
        })

    resume_data['Educational Details'] = educational_details

    # 3. Write data to a file
    with open("fakhir_resume.txt", "w") as resume_file:
        for key, value in resume_data.items():
            if key == 'Siblings':
                resume_file.write(f"{key}:\n")
                for item in value:
                    resume_file.write(f"  {item['name']}: {item['age']}\n")
            elif key == 'Educational Details':
                resume_file.write(f"{key}:\n")
                for item in value:
                    resume_file.write(f"  Level: {item['Level']}\n")
                    resume_file.write(f"  School Name: {item['School Name']}\n")
                    resume_file.write(f"  Degree: {item['Degree']}\n")
                    resume_file.write(f"  Years: {item['Years']}\n")
                    resume_file.write(f"  Passing Marks: {item['Passing Marks']}\n")
                    resume_file.write(f"  Total Marks: {item['Total Marks']}\n")
            else:
                resume_file.write(f"{key}: {value}\n")

    print("Resume created successfully!")

if __name__ == "__main__":
    main()

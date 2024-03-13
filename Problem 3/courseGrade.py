#Name: Xander Konell
#Hour: 3
def courseGrade(score):
    
    # TODO: Declare any necessary variables here. 
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'
      
def compute_average(scores):
    return sum(scores) / len(scores)
    # TODO: Read a file name from the user and read the tsv file here. 
def courseGrade():
    filename = input("Enter the tsv filename: ")
    students = []
    with open(filename, 'r') as f:
        for line in f:
            fields = line.strip().split('\t')
            last_name, first_name, midterm1, midterm2, final = fields
            midterm1 = int(midterm1)
            midterm2 = int(midterm2)
            final = int(final)
            students.append((last_name, first_name, midterm1, midterm2, final))
   
    # TODO: Compute student grades and exam averages, then output results to a text file here. 
    with open('report.txt', 'w') as f:
        for student in students:
            last_name, first_name, midterm1, midterm2, final = student
            avg_score = compute_average([midterm1, midterm2, final])
            letter_grade = compute_grade(avg_score)
            f.write(f"{last_name}\t{first_name}\t{midterm1}\t{midterm2}\t{final}\t{letter_grade}\n")
            
        exams = {'midterm1': [], 'midterm2': [], 'final': []}
        for student in students:
            exams['midterm1'].append(student[2])
            exams['midterm2'].append(student[3])
            exams['final'].append(student[4])

        avg_midterm1 = compute_average(exams['midterm1'])
        avg_midterm2 = compute_average(exams['midterm2'])
        avg_final = compute_average(exams['final'])

        f.write(f"\nAverages: midterm1 {avg_midterm1:.2f}, midterm2 {avg_midterm2:.2f}, final {avg_final:.2f}")
    return

if __name__ == "__main__":
    courseGrade()
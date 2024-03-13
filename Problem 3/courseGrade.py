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
      
    # TODO: Read a file name from the user and read the tsv file here. 
file_name = input("")
with open(file_name, 'r') as file:
    lines = file.readlines()
   
    # TODO: Compute student grades and exam averages, then output results to a text file here. 
midterm1_total = 0
midterm2_total = 0
final_total = 0
with open('report.txt', 'w') as report_file:
    for line in lines:
        data = line.split('\t')
       
        last_name = data[0]
        first_name = data[1]
       
        midterm1 = int(data[2])
        midterm2 = int(data[3])
        final = int(data[4])
      
        avg_score = (midterm1 + midterm2 + final) / 3
        letter_grade = compute_grade(avg_score)
        report_file.write(f"{last_name}\t{first_name}\t{midterm1}\t{midterm2}\t{final}\t{letter_grade}\n")
      
        midterm1_total += midterm1
        midterm2_total += midterm2
        final_total += final
    
    num_students = len(lines)
    midterm1_avg = midterm1_total / num_students
    midterm2_avg = midterm2_total / num_students
    final_avg = final_total / num_students
    
    report_file.write(f"\nAverages: midterm1 {midterm1_avg:.2f}, midterm2 {midterm2_avg:.2f}, final {final_avg:.2f}\n")

if __name__ == "__main__":
    courseGrade()
    
    
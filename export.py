from subject import Subject
import csv

def export_to_text(subject):
    pass

def export_to_csv(subject,filename):
    fields = ['名', '姓', '年龄', '性别']
    fields.append(subject.experiment.name)
    row = []    
    row.append(subject.firstname)
    row.append(subject.lastname)
    row.append(subject.age)
    row.append(subject.gender)
    for i in range(subject.experiment.N_sets):
        fields.append(f"试次{i+1}角度差")
        fields.append(f"试次{i+1}反应时间")

        row.append(subject.diff_in_rad[i])
        row.append(subject.reaction_time[i])

    with open(filename, 'w') as csvfile:  
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerow(row)
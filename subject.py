import csv
from collections import namedtuple
Experiment = namedtuple("Experiment",['name','N_sets'])

E1 = Experiment("1_normal",45)
E2 = Experiment("1_mirror",45)
E3 = Experiment("3_normal",70)
E4 = Experiment('4_mirror',70)

class IntervieweeNameError(Exception):
    pass

class GenderError(Exception):
    pass

class AgeError(Exception):
    pass

class Subject:
    def __init__(self, firstname, lastname, age, gender):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.gender = gender
        #self.experiment = experiment
        self.diff_in_rad = {}
        self.reaction_time = {}
        #for i in range(experiment.N_sets):
        #    self.diff_in_rad[i] = -1
        #    self.reaction_time[i] = -1

    def examine(self):
        flag = True
        if len(self.firstname)==0 or len(self.lastname)==0:
            raise IntervieweeNameError
        if not (self.gender=="男" or self.gender=="女"):
            raise GenderError
        if not(self.age.isdigit()):
            raise AgeError
        else:
            if int(self.age)!=float(self.age) or self.age<=0:
                raise AgeError

    # def insert_exp_result_into(self,reactiontime,)

    def export_to_csv(self,filename):
        fields = ['名', '姓', '年龄', '性别']
        fields.append(self.experiment.name)
        row = []    
        row.append(self.firstname)
        row.append(self.lastname)
        row.append(self.age)
        row.append(self.gender)
        for i in range(self.experiment.N_sets):
            fields.append(f"试次{i+1}角度差")
            fields.append(f"试次{i+1}反应时间")

            row.append(self.diff_in_rad[i])
            row.append(self.reaction_time[i])

        with open(filename, 'w') as csvfile:  
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(fields)
            csvwriter.writerow(row)
        
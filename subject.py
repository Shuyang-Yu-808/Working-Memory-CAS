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
        self.baseline_error = []

    def examine(self):
        flag = True
        if len(self.firstname)==0 or len(self.lastname)==0:
            raise IntervieweeNameError
        if not (self.gender=="男" or self.gender=="女"):
            raise GenderError
        if not(self.age.isdigit()):
            raise AgeError
        else:
            if int(self.age)!=float(self.age) or int(self.age)<=0:
                raise AgeError

    # def insert_exp_result_into(self,reactiontime,)

        
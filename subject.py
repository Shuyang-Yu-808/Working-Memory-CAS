import csv

class Subject:
    def __init__(self, firstname, lastname, age, gender,experiment_no):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.gender = gender
        self.diff_in_rad = []
        self.reaction_time = []
        self.experiment_no = experiment_no

    # def insert_into()

    # def export_cvs
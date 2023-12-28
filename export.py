from subject import Subject
import csv
from config import conf
from numpy import NaN
import logging
import datetime
import locale;
import os.path


file_exists = os.path.isfile(conf.csv_filename)

if locale.getpreferredencoding().upper() != 'UTF-8': 
    locale.setlocale(locale.LC_ALL, 'zh_CN.UTF-8') 
'''
This is a helper function that stores the experiment data
1. export_to_csv should be called when exiting the program without any anomalies
2. export_to_log should be called when exiting the program due to anomalies
'''

def export_to_csv(subject,filename):
    fields = ['姓', '名', '年龄', '性别', '测试时间']
    for i in range(1,11):
        fields.append('基线任务'+str(i))
    for i in range(1,conf.n_test_set_single_line+1):
        fields.append('正式任务'+str(i))
    row = []
    row.append(subject.lastname)
    row.append(subject.firstname)
    row.append(subject.age)
    row.append(subject.gender)
    row.append(str(datetime.datetime.now()))
    row.extend(subject.baseline_error+[NaN]*(10-len(subject.baseline_error)))
    row.extend(subject.maintask_error+[NaN]*(conf.n_test_set_single_line-len(subject.maintask_error)))
    with open(filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        if not file_exists:
            writer.writerow(fields)  
        writer.writerow(row)


def export_to_log(subject):
    row = []
    row.append(subject.firstname)
    row.append(subject.lastname)
    row.append(subject.age)
    row.append(subject.gender)
    row.extend(subject.baseline_error+[NaN]*(10-len(subject.baseline_error)))
    row.extend(subject.maintask_error+[NaN]*(conf.n_test_set_single_line-len(subject.maintask_error)))
    logging.basicConfig(filename="interrupt.log", level=logging.INFO)
    logging.error('['+str(datetime.datetime.now())+'] '+'Program exit due to keyboard interrupt'+str(row)) # More error to be implemented (if needed)

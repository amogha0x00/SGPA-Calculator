import numpy as np
import pandas as pd


def clac_grade_points(marks):
	grades = []
	print(marks)
	for sub_mark in marks:
		if sub_mark >= 90:
			grades.append(10)
		elif sub_mark >= 80:
			grades.append(9)
		elif sub_mark >= 70:
			grades.append(8)
		elif sub_mark >= 60:
			grades.append(7)
		elif sub_mark >= 45:
			grades.append(6)
		elif sub_mark >= 40:
			grades.append(5)
		else:
			grades.append(0)
	return np.array(grades)

def clac_sgpa(marks, sem):
	credit_sem_1 = [4, 4, 3, 3, 3, 1, 1, 1]
	credit_sem_2 = [4, 4, 3, 3, 3, 1, 1, 1]
	credit_sem_3 = [3, 4, 3, 3, 3, 3, 2, 2, 1]
	credit_sem_4 = [3, 4, 3, 3, 3, 3, 2, 2, 1]
	credit_sem_5 = [3, 4, 4, 3, 3, 3, 2, 2, 1]
	credit_sem_6 = [4, 4, 4, 3, 3, 2, 2, 2]
	credit_sem_7 = [3, 3, 3, 3, 3, 2, 2, 1]
	credit_sem_8 = [3, 3, 8, 1, 3]
	credits_dict = {1 : credit_sem_1, 2:credit_sem_2, 3:credit_sem_3, 4: credit_sem_4, 5: credit_sem_5, 6: credit_sem_6, 7:[], 8:[]} 
	grade_points = clac_grade_points(marks)
	print(grade_points)
	sem_credit = credits_dict[sem]
	return round(grade_points.dot(sem_credit) / sum(sem_credit), 2)

def get_results(path_to_html):
	results = pd.read_html(path_to_html)
	sem_index = len(results)
	sgpa_list = [] 
	for sem, sem_result in zip(range(sem_index, 0, -1), results):
		sem_result = sem_result.drop(index=0).sort_values(by=0, key=lambda x: [i[-2:] for i in x])
		tot = np.array([int(i) for i in list(sem_result[3])])
		#print('SEM ',str(sem), ' RESULT \n', sem_result)
		sgpa = clac_sgpa(tot, sem)
		print(tot)
		sgpa_list.append(sgpa)
		print('sgpa : ', sgpa, 'SEM ', str(sem), '\n---------------')
	print('Avg sgpa : ', sum(sgpa_list)/sem_index)
get_results('JAMS Student Master Record.html')
import numpy as np
import pandas as pd

def clac_grade_points(marks):
	grades = []
	print(f"marks: {marks}, total: {sum(marks)}")
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
	credits_dict = {1 : credit_sem_1, 2:credit_sem_2, 3:credit_sem_3, 4: credit_sem_4, 5: credit_sem_5, 6: credit_sem_6, 7:credit_sem_7, 8:credit_sem_8} 
	grade_points = clac_grade_points(marks)
	print(f"{grade_points=}")
	sem_credit = credits_dict[sem]
	sum_grades_without_f = 0
	for i, grade in enumerate(grade_points):
		if grade:
			sum_grades_without_f += sem_credit[i]
	credits_ob = grade_points.dot(sem_credit)
	return round( credits_ob / sum(sem_credit), 2), credits_ob, sum_grades_without_f
	# return 
def get_results(path_to_html):
	results = pd.read_html(path_to_html)
	sem_index = len(results)
	tot_credit_ob_list = []
	tot_grades_list_without_f = []
	for sem, sem_result in zip(range(sem_index, 0, -1), results):
		print(f"SEM: {sem}".center(30, "-"))
		#print(sem_result.drop(index=0).sort_values(by=0, key=lambda x: [i[-3:-1] if i[-3].isnumeric() else i[-2:] for i in x]))
		sem_result = sem_result.drop(index=0).sort_values(by=0, key=lambda x: [i[-3:-1] if i[-3].isnumeric() else i[-2:] for i in x])
		tot = np.array([int(i) for i in list(sem_result[3])])
		#print('SEM ',str(sem), ' RESULT \n', sem_result)
		sgpa, credits_ob, sum_grades_without_f = clac_sgpa(tot, sem)
		tot_credit_ob_list.append(credits_ob)
		tot_grades_list_without_f.append(sum_grades_without_f)

		print(f'\nSGPA: {sgpa}\n')
	cgpa = sum(tot_credit_ob_list)/sum(tot_grades_list_without_f)
	print(f"CGPA: {cgpa}")
	return cgpa

get_results('JAMS Student Master Record.html')

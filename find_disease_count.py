'''
Global Variables
'''
'''
d_file=open('disease.txt')

diseases_list = d_file.readlines()
temp_disease = []
'''
diseases_list = ['heart','parkinson','cancer','cardiovascular','kidney','metagenome','liver','breast',"parkinson's","alzheimer's",'skin','anemia','diabetes','hepatitis','HIV','atherosclerosis','intraocular','coronary','lung','pneumonia','TB','glaucoma','diabetic','covid-i9','alzheimer']

'''
Preprocessing the disease list
'''
'''
for w in diseases_list:
	w = w.lower()
	if w is '\n':
		continue
	else:
		temp_disease.append(w.rstrip('\n'))

print(temp_disease)

diseases_list = temp_disease
'''
'''
End of preprocessing

'''
diseases = {}
total_results=0
#
file_raw=open('raw.txt','r')
#
lines = file_raw.readlines()
for line in lines:
	try:
#		print('----------------------------------------------------------')
		words = line.split()
		total_results = total_results + 1
		for w in words:
			w = w.lower()
			if w in diseases_list:
				if w in diseases:
					diseases[w]=diseases[w]+1
				else:
					diseases[w]=1

	except Exception as e:
		raise e
#		finally:

'''
Save the output in the file

'''
file = open('scrap.txt','w')
file.write(str(diseases))
file.close()
file_raw.close()
print('____________________________________________')
for k in  sorted(diseases, key=diseases.get,reverse=True):
	print(k,":",diseases[k])
print('total results',total_results)

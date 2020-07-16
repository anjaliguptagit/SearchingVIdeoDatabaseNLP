from django.shortcuts import render
from django.http import HttpResponse
import os

def home(request):
	return render(request, 'search/home_file.html')
	
def results(request):
	if (request.method == 'POST'):
		data = 'yayyy'
		xyz = request.POST.get('query')
		os.system('python3 /media/anjali/0EFF08340EFF0834/SpeechRecog_ubuntu/Keywords/recipe_rake.py ' + xyz)
		res = {}
		with open("result.txt") as fp:
			lines = fp.readlines()
			for line in lines:
				line = line.strip()
				name = (line.split('/'))[0]
				res[name] = line
		#print(res)
		return render(request, 'search/results.html', {'res':res})
	else:
		data = 'noooo'
		return render(request, 'search/results.html', {'query': data})

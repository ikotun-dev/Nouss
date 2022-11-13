
from http.client import HTTPResponse
import re
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages 

#using time to delay rendering of a age so thatdata can load properly 
import time

t =  1
# Create your views here.
def home(request):
    # this is the index section 
    # the first page the user would see whenhe launches the server 

    #base is 127.0.0.1 on port 8000  
    return render(request, "my_virtual/index.html")
#this is the function for the signup section
#using the post method to 
def signup(request):
    if request.method ==  "POST" :
        username = request.POST['fname']
        secname = request.POST['sname']
        email = request.POST['email']
        passw = request.POST['password']

        #making the user to directly become a superuser 
        #making the user to directly become 
        # is_staff = True
        # is_superuser = True

    #    is_staff = True

        #for filtering the username registering to check  if it has already been in the database befre 
        if User.objects.filter(username=username):
            messages.error(request, "Username already exists, please try another one ")
    
        


        my_user = User.objects.create_user(username,email, passw)
        my_user.first_name = username
        my_user.last_name = secname
    

#~~~~~~~~~~~~~~~~~ saving the user into the database 
        my_user.save()

        return redirect('signin')

    return render(request, "my_virtual/signup.html")

# def signin(request):
#     return HttpResponse('<h1>Thus us also a testig ohase </h1>')


# { the function for signin in : }
def signin(request):  
    if request.method == "POST":
        username = request.POST['name']
        passw = request.POST['password']

        request.session['fname'] = username
        #first dictionary 

        context = { 
            'fname' : request.session['fname']
             }

        user = authenticate(username=username , password=passw)
        if user is not None:
            login(request, user)
            #fname = user.username
            #using the time.sleep function to delay the loading of the page
            time.sleep(t)
            return render(request, "my_virtual/addCourses.html", context)


        else:

            #when the user inputs a wrong detail || be it password or username - it redirects to the home page 
            msg = "Wrong Details.....return to login pagee"
            return HttpResponse(msg, content_type='text/plain')
            
            

            
    return render(request, "my_virtual/signin.html")

#{ the  add-courses function }
##this section is for the addCourses 
def addCourses(request):


    if request.method == "POST":
       course_1 = request.POST['course_1']
       course_2 = request.POST['course_2']
       course_3 = request.POST['course_3']
       course_4 = request.POST['course_4']
       course_5 = request.POST['course_5']
       course_6 = request.POST['course_6']
    #    course_7 = request.POST['course7']
       course_8 = request.POST['course_8']
       course_9 = request.POST['course_9']
       course_10 = request.POST['course_10']
       


        # using sessions to create global variables for the courses inputed by the user 

       request.session['course_1'] = course_1
       request.session['course_2'] = course_2
       request.session['course_3'] = course_3
       request.session['course_4'] = course_4
       request.session['course_5'] = course_5
       request.session['course_6'] = course_6
    #    request.session['course_7'] = course_7
       request.session['course_8'] = course_8
       request.session['course_9'] = course_9
       request.session['course_10'] = course_10
       
       

       
        #the context variable - is the dictionary which stores information i might want to use with my frontend 

       context_2 = {
           'c1' : request.session['course_1'],
           'c2' : request.session['course_2'],
           'c3' : request.session['course_3'],
           'c4' : request.session['course_4'],
           'c5' : request.session['course_5'],
           'c6' : request.session['course_6'],
           'c8' : request.session['course_8'],
           'c9' :  request.session['course_9'],
           'c10' : request.session['course_10'],
           'fname' : request.session['fname'],

          }

       time.sleep(0.1)
        
       return render(request, "my_virtual/addRooms.html", context_2)

    return render(request, "my_virtual/addCourses.html") 

def addRooms(request):

        #   context = {
        #    'c1' : request.session['course_1'],
        #    'c2' : request.session['course_2'],
        #    'c3' : request.session['course_3'],
        #    'c4' : request.session['course_4'],
        #    'c5' : request.session['course_5'],
        #    'c6' : request.session['course_6'],
        #    'c7' : request.session['course_7'],
        #    'c8' : request.session['course_8'],

        #   }
      
         if request.method == "POST":
            venue_1 = request.POST['venue_1']
            venue_2 = request.POST['venue_2']
            venue_3 = request.POST['venue_3']
            venue_4 = request.POST['venue_4']
            venue_5 = request.POST['venue_5']
            # using sessions to create global variables for the venues 
            request.session['venue_1'] = venue_1
            request.session['venue_2'] = venue_2
            request.session['venue_3'] = venue_3
            request.session['venue_4'] = venue_4
            request.session['venue_5'] = venue_5

            #creating a dictionary 
            #to the 
            context = {
                
                'v1' : request.session['venue_1'],
                'v2' : request.session['venue_2'],
                'v3' : request.session['venue_3'],
                'v4' : request.session['venue_4'],
                'v5' : request.session['venue_5'],
                'c1' : request.session['course_1'],
                'c2' : request.session['course_2'],
                'c3' : request.session['course_3'],
                'c4' : request.session['course_4'],
                'c5' : request.session['course_5'],
                'c6' : request.session['course_6'],
        #        'c7' : request.session['course_7'],
                'c8' : request.session['course_8'],
                'c9' : request.session['course_9'],
                'c10': request.session['course_10'],
                'fname' : request.session['fname'],

            }

            time.sleep(0.5)
            return render(request, "my_virtual/addTutor.html", context)


         return render(request, "my_virtual/addRooms.html")




#function for adding tutors 
def addTutor(request):



    if request.method == "POST":

        c1 = request.POST['c1_tutor']
        c2 = request.POST['c2_tutor']
        c3 = request.POST['c3_tutor'] 
        c4 = request.POST['c4_tutor']
        c5 = request.POST['c5_tutor']
        c6 = request.POST['c6_tutor']
   #     c7 = request.POST['c7_tutor']
        c8 = request.POST['c8_tutor']

        #setting the tutor names to become global 
        request.session['c1_tutor'] = c1
        request.session['c2_tutor'] = c2
        request.session['c3_tutor'] = c3
        request.session['c4_tutor'] = c4
        request.session['c5_tutor'] = c5      
        request.session['c6_tutor'] = c6
        request.session['c8_tutor'] = c8
    
        #creating dictionary to pass into other functions 
        context={
            'c1': request.session['c1_tutor'],
            'c2': request.session['c2_tutor'],
            'c3': request.session['c3_tutor'],
            'c4': request.session['c4_tutor'],
            'c5': request.session['c5_tutor'],
            'c6': request.session['c6_tutor'],
     #       'c7': request.session['c7_tutor'],
            'c8': request.session['c8_tutor'],
            'v1' : request.session['venue_1'],
            'v2' : request.session['venue_2'],
            'v3' : request.session['venue_3'],
            'v4' : request.session['venue_4'],
            'v5' : request.session['venue_5'],
            'c1' : request.session['course_1'],
            'c2' : request.session['course_2'],
            'c3' : request.session['course_3'],
            'c4' : request.session['course_4'],
            'c5' : request.session['course_5'],
            'c6' : request.session['course_6'],
        #   'c7' : request.session['course_7'],
            'c8' : request.session['course_8'],
            'c9' :  request.session['course_9'],
           'c10' : request.session['course_10'],
            'fname' : request.session['fname'],


            }

        time.sleep(0.5)
        return render(request, "my_virtual/addGroup.html",context)
    return render(request, "my_virtual/addTutor.html")


def addGroup(request):
    if request.method == "POST":
        g1 = request.POST['group_1']
        g2 = request.POST['group_2']
        g3 = request.POST['group_3']
        g4 = request.POST['group_4']

        request.session['g1'] = g1
        request.session['g2'] = g2
        request.session['g3'] = g3
        request.session['g4'] = g4

        context = {
            'c1': request.session['c1_tutor'],
            'c2': request.session['c2_tutor'],
            'c3': request.session['c3_tutor'],
            'c4': request.session['c4_tutor'],
            'c5': request.session['c5_tutor'],
            'c6': request.session['c6_tutor'],
            'fname' : request.session['fname'],
            'c8': request.session['c8_tutor'],
            'v1' : request.session['venue_1'],
            'v2' : request.session['venue_2'],
            'v3' : request.session['venue_3'],
            'v4' : request.session['venue_4'],
            'v5' : request.session['venue_5'],
            'c1' : request.session['course_1'],
            'c2' : request.session['course_2'],
            'c3' : request.session['course_3'],
            'c4' : request.session['course_4'],
            'c5' : request.session['course_5'],
            'c6' : request.session['course_6'],
            'c8' : request.session['course_8'],
            'c9' :  request.session['course_9'],
            'c10' : request.session['course_10'],
            'g1' : request.session['g1'],
            'g2' : request.session['g2'],
            'g3' : request.session['g3'],
            'g4' : request.session['g4'],

              
        }

        time.sleep(1)
        return render(request, "my_virtual/timetable.html", context)


    return render(request, "my_virtual/addGroup.html")
    
def genTable(request):


        return render(request, "my_virtual/timetable.html")
    
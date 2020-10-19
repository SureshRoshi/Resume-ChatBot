"""This Chatbot is developed using python and flask along with html and css to design an attractive resume.

Many Packages like pyttsx3 for text to speech and datetime to know the current time are used.

Resume Builder Chatbot is a conversational tool that can automate the process of designing CVs for the applicants. 

With the automation in this field, applicants with even no knowledge of making CVs can design an attractive and convincing CV."""
from flask import Flask,render_template,make_response

app = Flask(__name__)

#greeting message
from datetime import datetime
import pyttsx3

hour = datetime.now()
def welcome():
    h = hour.hour
    if h<12:
        greet="A very Good Morning!"
    elif h<17:
        greet="Good Afternoon!"
    else:
        greet="A rather late Good Evening!"
    print(greet)
    voice_msg([greet])
    print("I am Resume_Bot \nI can help you in providing CV for your bright career")
    voice_msg(["I am Resume Bot. I can help you in providing CV for you bright career!"])

# Function call to take the list of projects done by the individual as input
def project_list(project):
    project_details=[]
    voice_msg(["Share any of your project that gives weight to your resume"])
    project_title = input("Bot => Share any of your project that gives weight to your resume\nYou => ")
    voice_msg(["Give a brief description about the above mentiones project"])
    project_description = input("Bot => Give a brief description about the above mentioned project\nYou => ")
    project_details.append(project_title)
    project_details.append(project_description)
    project.append(project_details)
    voice_msg(["Enter your choice 1.Add another project 2.Next"])
    print("Bot => Enter your Choice\n      1.Add another project \n      2.Next")
    choice=int(input())
    if choice==1 :
        project_list(project)
    else:
        return

# Function call to take the skills acquired by an individual as user input
def skills_list(skills):
    voice_msg(["Technical Proficiencies you are good at"])
    skill=input("Bot => Technical Proficiencies you are good at\nYou =>")
    skills.append(skill)
    voice_msg(["Enter your choice  1.Add skill 2.Next"])
    print("Bot => Enter Your Choice\n      1.Add skill \n      2.Next")
    choice=int(input())
    if choice==1 :
        skills_list(skills)
    else:
        return

#Function to take all the details regarding applicant's eduacation as input from the user
def education_list(education):
    education_details=[]
    voice_msg(["Name of the Institution"])
    college =input("Bot => Name of the Institution\nYou => ")
    qualification = input("Bot => Qualification\nYou => ")
    voice_msg(["Enter the skills or achievements made by you during your graduation"])
    college_description = input("Bot => Enter the skills or achievements made by you during your graduation\nYou => ")
    education_details.append(college)
    education_details.append(qualification)
    education_details.append(college_description)
    education.append(education_details)
    voice_msg(["Enter your Choice 1.Add another education section 2.next"])
    print("Bot => Enter Your Choice\n      1.Add another Education Section \n      2.Next")
    choice=int(input())
    if choice==1 :
        education_list(education)
    else :
        return


#Speech recognization
def voice_msg(var):
    speak = pyttsx3.init()
    speak.setProperty('rate',170)
    voices = speak.getProperty('voices')
    speak.setProperty('voice',voices[0].id)
    for i in var:
        speak.say(i)
    speak.runAndWait()


def bot():
    welcome()
    voice_msg(["May I Know your good name please"])
    global username
    username = input("Bot =>  May I know your good name please \nYou => ")
    voice_msg(["Let me know your job title or designation"])
    global job
    job = input("Bot => Let me know your job title or designation\nYou => ")
    voice_msg(["Please enter your email Id"])
    global email
    email =input("Bot => Please enter your email Id \nYou => ")
    voice_msg(["Enter your mobile number"])
    global phno
    phno = input("Bot => Enter your mobile number \nYou => ")
    voice_msg(["Give an exclusive introduction about yourself"])
    global profile
    profile = input("Bot => Give an exclusive introduction about yourself\nYou => ")

    global project
    project=[]
    project_list(project)

    global skills
    skills=[]
    skills_list(skills)

    global education
    education=[]
    education_list(education)

bot()

@app.route('/')
def index():
    return render_template("index.html",username=username,job=job,email=email,phno=phno,profile=profile,project=project,skills=skills,education=education)


if __name__ == "__main__":
    app.run()
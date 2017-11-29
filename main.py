from flask import Flask, request, redirect, render_template
import os
import cgi
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env= jinja2.Environment(loader =jinja2.FileSystemLoader(template_dir), autoescape =True)

app= Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods =['GET','POST'])
def display_form():
    #get values from from
    #if valid, go to welcome page
    #if not return error messages on /

    if request.method == "GET":
        return render_template( 'index.html')

    if request.method == "POST":
        username = request.form['username'] 
        password = request.form['password']
        verify_password = request.form["verify_password"]
        email_optional = request.form["email_optional"]  

        user_error="" 
        if username == " " or len(username) >20 or len(username)<3: 
            user_error = "No spaces and between 3 and 20 characters." 
                                                           
        elif  password == ' ' or len(password)>20 or len(password)<3:
             pass_error = "No spaces and between 3 and 20 characters"
            
                                                            
        match_error=""
        if password != verify_password:
             match_error = "Passwords must match."
        
                                                           
        email_optional_error =""                                             
        elif "." not in email_optional  and "@" not in email_optional or len(email_optional) > 20 or len(email_optional)<3 :
            email_optional_error = " Needs valid email and no spaces and between 3 and 20 spaces"

        elif user_error or pass_error or match_error or email_optional_error:
            return render_template('index.html',user_error=user_error, pass_error=pass_error, 
            match_error=match_error, email_optional_error=email_optional_error)

        elif user_error:
            return render_template('index.html', user_error = user_error)

        elif not user_error and not pass_error and not email_optional_error:
            return render_template('welcome.html', username=username) 


app.run()
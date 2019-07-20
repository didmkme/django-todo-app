# TODO App with Django

TODO application with Django that allows login users to create, edit, and delete project.

## Requirements
- Download [Python](https://www.python.org/downloads/)
- Download [Pip](https://pypi.org/project/pip/)
- Create virtual environment    
```$ pip install virtualenv```  
```$ virtualenv venv```  
    Activate virtual environment:  
		- On Windows: ``` $ venv/Scripts/activate ```    
		- On macOS and Linux: ``` $ source env/bin/activate ```  
- İnstall Django  
``` $ pip install Django ```  

## Features  
- Requires user login 
  - Sign up page
  
  ![signup](https://user-images.githubusercontent.com/25441621/61580503-ab6c9f00-ab1b-11e9-8267-a36491faf36d.PNG)
  
  - Log in page
  
  ![login](https://user-images.githubusercontent.com/25441621/61580519-d7882000-ab1b-11e9-931c-924aff84dbd5.PNG)
  
  - Change password page
  
  ![changepassword](https://user-images.githubusercontent.com/25441621/61580542-08685500-ab1c-11e9-9306-c2a5e1586708.PNG)
  
- Create, update, delete project

- Create, update, delete issue

- View list of projects and issues  

## Running the Project Locally
First, clone the repository to your local machine:  

``` $ git clone https://github.com/didmkme/django-todo-app.git ``` 

Install the requirements:  

``` $ pip install -r requirements.txt ```  

Create the database: (Make sure you are in directory same as manage.py)  

``` $ python manege.py migrate ```  

Finally, run the development server:  

``` $ python manage.py runserver ```  

> The project will be available at 127.0.0.1:8000


## License

[MIT](https://choosealicense.com/licenses/mit/)

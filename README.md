If you haven't installed python yet, here is an instruction on how to set up everything correctly: <br>
https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-an-ubuntu-20-04-server

How to create a virtual python environment:

1. Pick a folder for a project
2. Use

```python -m venv venv``` for Windows or

```python3 -m venv venv``` for Linux.

3. Enter your vitrual environment ```source test/bin/activate``` for Linux or

```test/Scripts/activate.bat``` In Windows CMD 

```test/Scripts/Activate.ps1``` In Windows Powershell

How to clone project to your virtual environment:

1. ```git clone https://github.com/JuicyS8da/Django_pilot``` (to your folder)
2. ```cd backend/```
3. ```pip install -r requirements.txt```
4. ```python manage.py runserver```
5. Put http://127.0.0.1:8000/ into url field in your browser
6. (optional) If you want to user django admin http://127.0.0.1:8000/admin/, default superuser is:

Login: user
Password: 123 (or 123123)

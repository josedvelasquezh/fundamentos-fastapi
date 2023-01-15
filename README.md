source venv/Scripts/activate

pip install fastapi
pip install uvicorn

pip install python-multipart

#Levantar API
uvicorn main:app --reload

pip install email-validator

#home
http://localhost:8000/

#swagger
http://localhost:8000/docs#/

#redoc
http://localhost:8000/docs#/
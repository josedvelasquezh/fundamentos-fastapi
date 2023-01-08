source venv/Scripts/activate

pip install fastapi
pip install uvicorn

#Levantar API
uvicorn main:app --reload


#home
http://localhost:8000/

#swagger
http://localhost:8000/docs#/

#redoc
http://localhost:8000/docs#/
source venv/Scripts/activate

pip install fastapi
pip install uvicorn

#Levantar API
uvicorn main:app --reload

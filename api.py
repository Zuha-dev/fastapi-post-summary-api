from fastapi import FastAPI
from data_layer import fetch_data
from processing import search_and_summarize

app = FastAPI()

@app.get("/users/summary/{user_id}")
def get_summary(user_id:int , keyword: str=None, min_length: int=None):

    try:
        data = fetch_data()
        result = search_and_summarize(data,user_id=user_id, keyword=keyword, min_length=min_length)

        return {
            "status": "success",
            "data": result
        }
        
    except Exception:
        return {
            "status": "error",
            "message": "something went wrong"
        } 
    


        
    

    


        

    





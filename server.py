from fastapi import FastAPI

api =  FastAPI()

@api.get('/')
async def main():
    return {'message':'aooba'}
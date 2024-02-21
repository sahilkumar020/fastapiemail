from fastapi import APIRouter

from models.todos import Todo   
from config.database import collection_name
from schema.schema import list_serial
from bson import ObjectId

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

router = APIRouter()

#GET REQ METHOD
@router.get("/")
async def get_todos():
    todos = list_serial(collection_name.find())
    return todos

#POST REQ METHOD
# @router.post("/")
# async def post_todo(todo: Todo):
#     collection_name.insert_one(dict(todo))

@router.post("/")
async def post_todo(todo: Todo):
    # Insert the todo into MongoDB
    result = collection_name.insert_one(todo.dict())

    # If the insertion is successful, send an email
    if result.inserted_id:
        await send_todo_added_email(todo)

    return {"message": "Todo added successfully"}

async def send_todo_added_email(todo: Todo):
    #       
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "hulk34741@gmail.com"
    smtp_password = "ndweermiwsreywsw"

    # Sender and recipient email addresses
    sender_email = "hulk34741@gmail.com"
    recipient_email = "sssahilkumar1@gmail.com"

    # Create a message object
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = "Todo added"

    # Add the todo message to the email body
  
    body = f"Todo added:\n\nTitle: {todo.name}\nDescription: {todo.description}"

    message.attach(MIMEText(body, "plain"))

    # Connect to the SMTP server and send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, recipient_email, message.as_string())

    print("Todo added email sent to sssahilkumar1@gmail.com")


#PUT REQ METHOD
@router.put("/{id}")
async def  put_todo(id : str, todo: Todo):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set":dict(todo)})

#DELET REQ METHOD
@router.delete("/{id}")
async def put_todo(id : str ):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})



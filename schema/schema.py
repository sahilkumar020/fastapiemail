def indivisual_serial(todo) -> dict:
    return{
        "id": str(todo["_id"]),
        "name": todo["name"],
        "description": todo["description"],
        "complete": todo["complete"]
    }

def list_serial(todos) -> dict:
    return[indivisual_serial(todo) for todo in todos]
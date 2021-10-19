def courseEntity(course) -> dict:
    return {
        "id": str(course["_id"]),
        "name": course["name"],
        "description": course["description"],
        "price": course["price"],
        "tags": course["tags"],
        "images": course["images"],
        "creationDate": course["creationDate"],
        "lastModificationDate": course["lastModificationDate"]
    }

def coursesEntity(courses) -> list:
    return [courseEntity(course) for course in courses]
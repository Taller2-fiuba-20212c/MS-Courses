def courseEntity(course) -> dict:
    return {
        "id": str(course["_id"]),
        "name": course["name"],
        "description": course["description"],
        "tags": course["tags"],
        "creationDate": course["creationDate"],
        "lastModificationDate": course["lastModificationDate"]
    }

def coursesEntity(courses) -> list:
    return [courseEntity(course) for course in courses]
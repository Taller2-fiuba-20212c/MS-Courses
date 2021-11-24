def courseEntity(course) -> dict:
    return {
        "id": str(course["_id"]),
        "name": course["name"],
        "description": course["description"],
        "tags": course["tags"],
        "units": course["units"],
        "exams": course["exams"],
        "consults": course["consults"],
        "teachers": course["teachers"],
        "collaborators": course["collaborators"],
        "students": course["students"],
        "suscriptionIncluded": course["suscriptionIncluded"],
        "image": course["image"],
        "published": course["published"],
        "creatorId": course["creatorId"],
        "creationDate": course["creationDate"],
        "lastModificationDate": course["lastModificationDate"]
    }

def coursesEntity(courses) -> list:
    return [courseEntity(course) for course in courses]
def examModelEntity(exam) -> dict:
    return {
        "id": str(exam["_id"]),
        "name": exam["name"],
        "description": exam["description"],
        "examQuestions": exam["examQuestions"],
        "creationDate": course["creationDate"],
        "lastModificationDate": course["lastModificationDate"]
    }

def coursesEntity(courses) -> list:
    return [courseEntity(course) for course in courses]
def postEntity(item) -> dict:
    return {
            "id":           str(item["_id"]),
            "book": str(item["book"]),
            "author":item["author"],
            "categories":   item["categories"],
            "body":         item["body"],
            "rate":         item["rate"]
            }

def postsEntity(entity) -> list:
    return [postEntity(item) for item in entity]


import pymongo

def get_keywords(user_name, password, db_name, text_list):
    connection_url = "mongodb+srv://"+user_name+":"+password+"@cluster0.43xkd.mongodb.net/"+db_name+"?retryWrites=true&w=majority"
    client = pymongo.MongoClient(connection_url)
    db = client.keyword_db
    collection = db.keyword_collection
    find = collection.find()
    keyword_count = {}
    for doc in find:
        word = doc["word"]
        if word == "":
            continue
        keyword = doc["keyword"]
        if keyword not in keyword_count.keys():
            keyword_count[keyword] = 0
        for text in text_list:
            keyword_count[keyword] += text.count(word)
    print(keyword_count)



if __name__ == "__main__":
    get_keywords()
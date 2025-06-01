

import pymongo


def message_data(name,email,message):
    client = pymongo.MongoClient("mongodb+srv://dubeysaksham796:Iron_Man@adhyayancoachinginstitu.hqcuhrf.mongodb.net/?retryWrites=true&w=majority&appName=AdhyayanCoachingInstitute")
    db = client['Adhyayan_Coaching_Institute']
    collection = db['message']


    dict = {}
    dict['name'] = name
    dict['email'] = email
    dict['message'] = message


    collection.insert_one(dict)



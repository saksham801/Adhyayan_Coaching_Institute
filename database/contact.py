

import pymongo


def contact_data(name,email,phone_no,message):
    client = pymongo.MongoClient("mongodb+srv://dubeysaksham796:Iron_Man@adhyayancoachinginstitu.hqcuhrf.mongodb.net/?retryWrites=true&w=majority&appName=AdhyayanCoachingInstitute")
    db = client['Adhyayan_Coaching_Institute']
    collection = db['contact']


    dict = {}
    dict['name'] = name
    dict['email'] = email
    dict['phone_no'] = phone_no
    dict['message'] = message

    collection.insert_one(dict)



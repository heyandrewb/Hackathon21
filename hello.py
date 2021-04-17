import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# initializations
cred = credentials.Certificate('festive-bloom-310805-firebase-adminsdk-6aycz-67bf2fb938.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

emp_ref = db.collection('users')
docs = emp_ref.stream()

for doc in docs:
    print('{} => {} '.format(doc.id, doc.to_dict().lastName))
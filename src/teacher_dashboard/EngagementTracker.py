import firebase_admin
from firebase_admin import db

firebase_admin.initialize_app()

def log_engagement(student_id, activity):
    ref = db.reference(f'engagement/{student_id}')
    ref.push({
        'activity': activity,
        'timestamp': datetime.now().isoformat()
    })


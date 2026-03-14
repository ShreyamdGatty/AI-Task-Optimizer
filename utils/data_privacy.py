import hashlib

def anonymize_employee(name):

    hashed = hashlib.sha256(name.encode()).hexdigest()

    return hashed

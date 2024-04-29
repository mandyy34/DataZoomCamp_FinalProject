from hashlib import sha1

def compute_hash(email):
    return sha1(email.encode('utf-8')).hexdigest()

def compute_certificate_id(email):
    email_clean = email.lower().strip()
    return compute_hash(email_clean + '_')


cohort = 2024
course = 'dezoomcamp'
your_id = compute_certificate_id('ymyau6@gmail.com')
url = f"https://certificate.datatalks.club/{course}/{cohort}/{your_id}.pdf"
print(url)


# https://certificate.datatalks.club/dezoomcamp/2024/d779b84accde6e0c6957e2fb40b44f25916748f3.pdf
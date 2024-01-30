import urllib.request, bs4, smtplib, time

hermes = 'https://www.hermes.com/ca/en/search/?s=Evelyne%2016%20Amazone#'

def isEvelyneThere():
    # read the response (html)
    sauce = urllib.request.urlopen(hermes).read()
    # convert it to readable html
    soup = bs4.BeautifulSoup(sauce, "html.parser")
    # find the span with 
    no_result = soup.find('h1', {'class': 'no-result'})
    if no_result:
        return False
    else:
        product = soup.find('span', {'class': 'product-item-name'})
        if product:
            return True
    return False

def send_email(message, sender_email, sender_password, receiver_email):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(sender_email, sender_password)
    s.sendmail(sender_email, receiver_email, message)
    s.quit()

while True:
    has_product = isEvelyneThere()
    if has_product:
        message = f"Evelyne is on Hermes NOW!"
        send_email(message) #ADD THE OTHER AGRUMENTS sender_email, sender_password, receiver_email
    time.sleep(43000)
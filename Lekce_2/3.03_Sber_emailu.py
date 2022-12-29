my_str = ["parrt10@yahoo.ca", "koudas@mac.com",
    "shaffei@yahoo.com", "dwendlan@optonline.net",
    "catalog3@optonline.net", "paley@gmail.com",
    "ullman@outlook.com", "mgreen@verizon.net",
    "lamprecht@live.com", "frost666man@icloud.com",
    "nullchar@yahoo.com", "lermanab@live.com",
          "konec", "65", "nic"]

emaily = {}
with_numbers = {}
domains = {}


def email(vstup):
    for slovo in vstup:
        if "@" in slovo:
            emaily.setdefault(slovo)
    return emaily.keys()

def domeny(vstup):
    for slovo in emaily:
        slovo = slovo.split("@")[-1]
        domains.setdefault(slovo)
    return domains.keys()

def with_num(vstup):
    for slovo in emaily:
        for pismeno in slovo:
            if pismeno.isdigit():
                with_numbers.setdefault(slovo)
    return with_numbers.keys()


# jádro funkce pro scůj chod použije všechny tři předchozí funkce
# problém se slovníky.. pokud to dám jako set tak mi to adresy s čísly hodí tolikrát kolik mají v sobě čísel
# asi se to dá obejít.. použil jsem ale slovník.. ten to eliminuje ale vypíše se do finálního řešení..
def main():
    result = {'emails_with_nums': None,
              'domains': None}
    emaily = email(my_str)
    result['emails_with_nums'] = with_num(emaily)
    result['domains'] = domeny(emaily)
    print(result)
    return result



#print(email(my_str))
#print(domeny(domains))
#print(with_num(emaily))

#funkci main stačí zevolat bez printu.. ve funkci samotné už print je takže buď ho necháme tam
# nebo ho musíme napsat pokaždé, když budeme chtít zavolat funkci
main()



###########  ŘEŠENÍ ENGETO

# Funkce pro posbirani emailu ze stringu
# v případě, že se jedná o string.. já už použil set takže jsem to neřešil.. jinak snadné jen .split..
def collect_emails(text):
    words =  text.split()
    emails = []
    for word in words:
        if '@' in word:
            emails.append(word)
    return emails

# Funkce pro extrahovani emailu obsahujici cisla

# Eliminace mého problému s násobným zapsáním adres s čísly..
def select_num_emails(emails):
    num_mails = []
    for email in emails:
        if contains_number(email):
            num_mails.append(email)
    return num_mails


def contains_number(_string):
    for num in range(10):
        if str(num) in _string:
            return True
    return False
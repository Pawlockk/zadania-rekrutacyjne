import time
from elephant import *

db_name = "Baza_pyth"


create_database(db_name)

time.sleep(2) #sleep po to, że baza nie istnieje w momencie próby połączenia się z nią

connect(db_name)




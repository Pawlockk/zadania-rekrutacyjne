import time
from elephant import *

db_name = "Baza_pyth"


create_database(db_name)

time.sleep(5) #sleep po to, że baza nie istnieje w momencie próby połączenia się z nią bo API elephantSQL jest za wolne XDD

connect(db_name)

create_tables()

fill_tables()

queries()

update_tables()

delete()



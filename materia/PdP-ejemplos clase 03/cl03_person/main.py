from worker import Worker
from person import Person


persons = [Person('Juan'), Person('Pedro'), Worker('Ana', 'UANDES'),
           Person('María'), Worker('Paz', 'EMOL')]

for p in persons:
    print(p.greet())
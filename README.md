# utils

Drobne narzędzia wielokrotnego użytku.

## pagination.py

`paginate(items, page=1, limit=50)` zwraca jedną stronę listy razem z liczbą wszystkich pozycji i stron.

```python
from pagination import paginate

wynik = paginate(list(range(120)), page=2, limit=50)
# {'data': [50, ..., 99], 'page': 2, 'limit': 50, 'total': 120, 'total_pages': 3}
```

Strony liczone są od 1. Lista pusta daje jedną stronę bez danych (`total_pages` wynosi co najmniej 1).

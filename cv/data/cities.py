from django.db import models

class JobLocation(models.TextChoices):
    BAGHDAD = 'BAGHDAD', 'Baghdad'
    BASRAH = 'BASRAH', 'Basrah'
    ARBIL = 'ARBIL', 'Arbil'
    SULAYMANIYAH = 'SULAYMANIYAH', 'Sulaymaniyah'
    KARKH = 'KARKH', 'Karkh'
    KARBALA = 'KARBALA', 'Karbala'
    NAJAF = 'NAJAF', 'Najaf'
    RAMADI = 'RAMADI', 'Ramadi'
    HILLAH = 'HILLAH', 'Hillah'
    NASIRIYAH = 'NASIRIYAH', 'Nasiriyah'
    DUHOK = 'DUHOK', 'Duhok'
# Boverket Vägbuller

Uppskatta vägbuller enligt schabloner från Boverket (https://www.boverket.se/globalassets/publikationer/dokument/2016/hur-mycket-bullrar-vagtrafiken_low.pdf).

```python
from boverket_buller import vagbuller

vagbuller(hastighet,adt,avstand, mjuk_mark = False)
"""
Uppskatta väbuller enligt Boverkets schabloner

Parameters:
hastighet: Skyltad hastighet, km/h
adt: Traffikmängd, fordon/dygn
avstand: Avstånd vägmitt i meter
mjuk_mark: Är det dominarande mjuk mark mellan väg och mottagare

Returns:
float: vägbullernivå i dBA
"""
```


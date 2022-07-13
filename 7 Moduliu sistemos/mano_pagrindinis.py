import mano_modulis

sakinys = "Sveikas, pasauli!"
atbulai = mano_modulis.parasyti_atbulai(sakinys)

# mano_modulis sėkmingai importuotas!
# !iluasap ,sakievS

import mano_modulis as mm

sakinys = "Sveikas, pasauli!"
atbulai = mm.parasyti_atbulai(sakinys)

# mano_modulis sėkmingai importuotas!
# !iluasap ,sakievS

from mano_modulis import parasyti_atbulai

sakinys = "Sveikas, pasauli!"
atbulai = parasyti_atbulai(sakinys)

# mano_modulis sėkmingai importuotas!
# !iluasap ,sakievS

from mano_modulis import parasyti_atbulai, kintamasis

sakinys = "Sveikas, pasauli!"
atbulai = parasyti_atbulai(sakinys)
print(kintamasis)

# mano_modulis sėkmingai importuotas!
# !iluasap ,sakievS
# Čia yra testinis kintamasis

from mano_modulis import parasyti_atbulai as pa, kintamasis

sakinys = "Sveikas, pasauli!"
atbulai = pa(sakinys)
print(kintamasis)

# mano_modulis sėkmingai importuotas!
# !iluasap ,sakievS
# Čia yra testinis kintamasis

from mano_modulis import *

sakinys = "Sveikas, pasauli!"
atbulai = parasyti_atbulai(sakinys)
print(kintamasis)

# mano_modulis sėkmingai importuotas!
# !iluasap ,sakievS
# Čia yra testinis kintamasis

import moduliai.mano_modulis_3 as mm3
print(mm3.kintamasis3)

# mano_modulis_3 sėkmingai importuotas!
# Čia yra testinis kintamasis 3
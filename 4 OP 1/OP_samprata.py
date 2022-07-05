# Programavimo samprata
# Programavimas – tai objektų bei uždavinio sprendimo 
# eigos aprašymas programavimo kalboje.
# Sudėtingi uždaviniai reikalauja papildomų etapų:
# uždavinio analizės,
# sprendimo būdo ir kelio parinkimo,
# suderinimo su užsakovu,
# sprendimo algoritmo aprašymo,
# jo pavertimo programa,
# programos testavimo ir derinimo,
# bandomosios eksploatacijos, ...
# ====================================================
# Programavimo etapai
# 1. Problemos aprašymas.
# 2. Algoritmo parinkimas (sudarymas).
# 3. Kodavimas pasirinkta programavimo kalba.
# 4. Programos kompiliavimas, derinimas ir testavimas.
# 5. Programos diegimas ir eksploatavimas.
# ====================================================
# Programos kodo kompiliavimas:
# Programos sintaksės ir semantikos tikrinimas.
# Transliavimas į žemo lygio kalbą.
# Vykdomojo programos failo sukūrimas.
# ====================================================
# Programos derinimas ir testavimas
# Klaidų aptikimas ir ištaisymas.
# Programos vykdymas su įvairiais duomenų rinkiniais ir rezultatų analize.
# ====================================================
# Objektinis programavimas (OP), programavimo kalbos
# ====================================================
# Esmė
# ====================================================
# Pagrindinė OP idėja – duomenų ir jais operuojančių funkcijų apjungimas 
# į vieną visumą (objektą):
# objekto duomenys išorėje tiesiogiai neprieinami, 
# tik per juos nuskaitantį objekto sąsajos metodą
# jei reikia keisti objekto duomenis, kreipiamės į juos įrašantį 
# objekto sąsajos metodą.
# ====================================================
# Duomenų ir juos apdorojančių funkcijų apjungimas į vieną visumą 
# ir paslėpimas nuo išorės vadinamas inkapsuliacija.
# Tai leidžia neprisirišti prie konkrečios objekto realizacijos.
# ====================================================
# Objektinis programavimas – programavimo būdas, 
# naudojant objektus ir jų sąveikas
# Objektas – į vieną vienetą (klasę) 
# sutalpintos susijusios savybės ir funkcionalumas 
# (kintamieji, funkcijos ir t.t.)
# ====================================================
# Programavimo kalboje – kintamieji.
# Daug vienos rūšies duomenų: atmintinės laukai 
# nuosekliai išdėstytoms vieno tipo reikšmėms.
# Programavimo kalboje – masyvai.
# Daug skirtingų rūšių duomenų: 
# atmintinės laukai nuosekliai išdėstytoms skirtingų tipų reikšmėms. 
# Programavimo kalboje – klasės.
# Objektų masyvai, masyvai klasėse, ...
# Dinaminiai duomenys, indeksai, katalogai, ryšiai ...
# Duomenys išoriniuose informacijos nešėjuose – failų sistemos.
# Objektinis programavimas išpopuliarėjo paskutiniame XX amžiaus dešimtmetyje. 
# Objektinio programavimo populiarumo priežastis – sąsajos su natūraliais gamtos objektais ir reiškiniais. 
# Pagrindinė idėja – realaus pasaulio objektų (jų savybių ir elgsenos) bei manipuliavimo objektais procesų aprašymas. 
# Pagrindinis požymis – savybių (duomenų) ir elgsenos (programų) apjungimas objektuose, galimybė operuoti objektais bei jų dalimis.
# Objektiniame programavime informacija slepiama nuo išorės (inkapsuliacija). 
# Tai leidžia kurti universalesnes programas, 
# neprisirišant prie objektų realizacijos būdo, 
# lengviau programą modifikuoti.
# Klasės apjungiamos į hierarchijas paveldėjimo principu.
# Polimorfizmas – gebėjimas adaptuotis pagal aplinką.
# Gali būti kuriamos specializuotos klasės.
# Objektinio programavimo privalumai išryškėja dideliuose projektuose, 
# kai dirba daug žmonių.
# Klasė – tai duomenų tipas, nusakantis objekto:
# - savybes: tai kintamieji (duomenys).
# - elgseną: tai funkcijos (metodai).
# Objektas – tai klasės tipo kintamasis. 
# Objektas turi duomenis ir darbo su jais metodus.
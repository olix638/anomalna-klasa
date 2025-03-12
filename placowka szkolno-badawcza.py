print("bezpiecznie\n"
      "niebezpiecznie\n"
      "ok\n"
      "o nie\n"
      "jest źle")
while True:
    co_chcesz = input("co chcesz zrobić? (opowieść, obiekty) ")
    if co_chcesz == "opowieść":
        jaką_chcesz_opowieść = input("jaką opowieść chcesz przeczytać? ")
        if jaką_chcesz_opowieść == "kim jestem?":
            pass
    elif co_chcesz == "obiekty":
        obiekt = int(input("jaki obiekt chcesz zobaczyć(1-3)? "))
        if obiekt == 1:
                print("\nnazwa obiektu: śmierć\n"
                    "klasa obiektu: jest źle\n"
                    "opis obiektu:\n"
                    "jest cały czarny\n"
                    "ma kosę\n"
                    "puste oczy\n"
                    "wielki płaszcz\n"
                    "umiejętnoiści obiektu:\n"
                    "jest nieśmiertelny\n"
                    "widzi [USUNIĘTO]\n"
                    "każdy kto go zobozczy kończy się zgonem przez wykrwawienie albo dożywotnie zniszczona spyhika\n"
                    "ma umiejętności hipnotyczne\n"
                    "naśladowanie głosów\n"
                    "Dodatki:\n"
                    "dedatek 1:\n"
                    "dr.Lars+: no dobra, gadamy z obiektem 1\n"
                    "cisza przez 2 minuty\n"
                    "dr.Lars+:słuchasz mnie\n"
                    "obiekt 1: cały swoim ciałem\n"
                    "dr.Lars+:co widzisz\n"
                    "obiekt 1: widzę [USUNIĘTO]\n"
                    "ale jak to przecież jesteś w pokuju\n"
                    "ja zawsze widzę [USUNIĘTO]\n"
                    "ale ja niechce być śmiercią\n"
                    "nie chce być śmiercią\n"
                    "dr.+:obiekcie wszystko ok\n"
                    "obiekt 1: nie\n"
                    "dr.Lars+:co się stało\n\n"
                    "później obiekt 1 zaczął krzyczeć i jakims cudem zamordował 36 badaczy\n"
                    "do tej pory nie wiadomo jak to zrobił\n"
                    "Dodatek 2:\n"
                    "przerażony obiekt 1 samym sobą Nareście mówił kim jest\n\n"
                    "[DIALOG USUNIĘTO]\n"
                    "Dodatek 3:\n"
                    "Dziś się zmienia dajemy człowieka\n"
                    "\ndr.[USUNIĘTO]: witam [USUNIĘTO]\n"
                    "obiekt 1: kim jestem\n"
                    "dr.[USUNIĘTO]: jesteś śmiercią\n"
                    "obiekt 1: nie chce być śmiercią\n"
                    "dr.[USUNIĘTO]: to nie jest twoja decyzja\n"
                    "obiekt 1: HAHAHAHAHA myśleliście że mnie nabraliście on już dawno zginą a wy nic\n"
                    "\nwtedy dowiedziano że obiekt 1 umie naśladować głosy innych\n"
                    "dziękuję za przeczytanie\n"
                    "opowieści o obiekcie 1:śmierć\n")
        elif obiekt == 2:
            print("nazwa obiektu: duolingo\n"
                "klasa obiektu: bezpicznie/zabawny\n"
                "opis obiektu:\n"
                "jest Sową\n"
                "jest przeklęty w aplikacji\n"
                "jest strasznie wciekły\n"
                "umiejętności obiektu:\n"
                "umie gadać w każdym języku świata\n"
                "może przejść do prawdziwego świata jak za długo grasz\n"
                "")
        else:
            print("nie ma takiego obiektu")
    else:
        print("nie ma takiej rzeczy")
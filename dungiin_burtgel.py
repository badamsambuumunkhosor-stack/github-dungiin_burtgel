with open("ners.txt", "w", encoding="utf-8") as f:
    f.write("Suhe,98,eregtei\n")         
    f.write("Saraa,98,emegtei\n")
    f.write("Temka,95,eregtei\n")
    f.write("Ali,96,eregtei\n")
    f.write("Nandia,93,emegtei\n")
    f.write("Nomio,95,emegtei\n")
    f.write("Tugsuu,90,eregtei\n")
    f.write("Batuka,98,eregtei\n")
    f.write("Saruul,97,emegtei\n")
    f.write("Bulgaa,93,eregtei\n")


NERSUUD_FILE = "ners.txt"

def huuhduud(file_ner):
    result = []
    with open(file_ner, "r") as f:
        for mur in f:
            mur = mur.strip()
            if mur == "":
                continue
            bmur = mur.split(",")
            result.append({"ner": bmur[0], "dungiin_golc": int(bmur[1]), "huis": bmur[2]})
    return result

def huuhduud_jagsaalt(nersuud):
    num = 1
    for ners in nersuud:
        print(num,".",ners["ner"],ners["dungiin_golc"],ners["huis"])
        num +=1

def huuhed_haih(nersuud, ner):
    for ners in nersuud:
        if ners["ner"] == ner:
            return ners
    return None

def huuhduud_huis(nersuud, huis):
    result = []
    for ners in nersuud:
        if ners['huis'] == huis:
            result.append(ners["ner"])
    return result

def huuhduud_dun(nersuud, dungiin_golc):
    for ners in nersuud:
        if ners["dungiin_golc"] == dungiin_golc:
            return ners
    return None
if __name__ == "__main__":
    nersuud = huuhduud(NERSUUD_FILE)

    if not nersuud:
        print(f"Ner baihgui bna! Dahij ner hai!")
    else:
# hailt = []
# while != 0 :
        while True:
            print("---Dungiin Jagsaalt---")
            print("1 - Suragcdiin ners")
            print("2 - Suragcdiin huis")
            print("3 - Dungiin golc")
            print("4 - Duusgah")
            songolt = input("Tanii songolt (1-4): ").strip()
            if songolt == "1":
                huuhduud_jagsaalt(nersuud)
            elif songolt == "2":
                huis = input("huis (eregtei/emegtei): ")
                huisuud = huuhduud_huis(nersuud, huis)
                if huisuud:
                    for ner in huisuud:
                        print("-", ner)
                else:
                    print("Huisee zov bicsen eseh")
            elif songolt == "3":
                # dun = input("Huuhdiin ner: ").strip()
                ner = input("Huuhdiin ner: ").strip()
                huuhed = huuhed_haih(nersuud,ner)
                if huuhed:
                    print(huuhed["ner"],"-",huuhed["dungiin_golc"])
                # if dun in nersuud:
                    # print("dun", "-", dun["dungiin_golc"])
                else:
                    print("Ner zov bicsen eseh!")
            elif songolt == "4":
                print("Duuslaa!")
                break
            else:
                print("Zovhon 1-4 hurtel!!!")
        





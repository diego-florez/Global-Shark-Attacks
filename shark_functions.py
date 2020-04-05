import re

def shark_species(data):
    clean_species = []

    for s in data:

        clean = re.sub(r"(.*)?whitetip(.*)?", "whitetip", s)
        clean = re.sub(r"(.*)?tiger(.*)?", "tiger", clean)
        clean = re.sub(r"(.*)?bull(.*)?", "bull", clean)
        clean = re.sub(r"(.*)?nurse(.*)?", "nurse", clean)
        clean = re.sub(r"(.*)?whaler(.*)?", "whaler", clean)
        clean = re.sub(r"(.*)?blacktip(.*)?", "blacktip", clean)
        clean = re.sub(r"(.*)?reef(.*)?", "reef", clean)
        clean = re.sub(r"(.*)?mako(.*)?", "mako", clean)
        clean = re.sub(r"(.*)?raggedtooth(.*)?", "raggedtooth", clean)
        clean = re.sub(r"(.*)?wobbegong(.*)?", "wobbegong", clean)
        clean = re.sub(r"(.*)?spinner(.*)?", "spinner", clean)
        clean = re.sub(r"(.*)?hammerhead(.*)?", "hammerhead", clean)
        clean = re.sub(r"(.*)?blue(.*)?", "blue", clean)
        clean = re.sub(r"(.*)?lemon(.*)?", "lemon", clean)
        clean = re.sub(r"(.*)?zambesi(.*)?", "zambesi", clean)
        clean = re.sub(r"(.*)?sandtiger(.*)?", "sandtiger", clean)
        clean = re.sub(r"(.*)?sandbar(.*)?", "sandbar", clean)
        clean = re.sub(r"(.*)?sevengill(.*)?", "sevengill", clean)
        clean = re.sub(r"(.*)?dusky(.*)?", "dusky", clean)
        clean = re.sub(r"(.*)?carpet(.*)?", "carpet", clean)
        clean = re.sub(r"(.*)?angel(.*)?", "angel", clean)
        clean = re.sub(r"(.*)?galapagos(.*)?", "galapagos", clean)
        clean = re.sub(r"(.*)?basking(.*)?", "basking", clean)
        clean = re.sub(r"(.*)?gill(.*)?", "gill", clean)
        clean = re.sub(r"(.*)?porbeagle(.*)?", "porbeagle", clean)
        clean = re.sub(r"(.*)?copper(.*)?", "copper", clean)
        clean = re.sub(r"(.*)?colored(.*)?", "colored", clean)
        clean = re.sub(r"(.*)?dog(.*)?", "dog", clean)
        clean = re.sub(r"(.*)?silky(.*)?", "silky", clean)
        clean = re.sub(r"(.*)?white(.*)?", "white", clean)
        clean = re.sub(r"(.*)?sand(.*)?", "sand", clean)
        clean = re.sub(r"(.*)?zambezi(.*)?", "zambezi", clean)
        clean = re.sub(r"(.*)?thresher(.*)?", "thresher", clean)
        clean = re.sub(r"(.*)?salmon(.*)?", "salmon", clean)
        clean = re.sub(r"(.*)?involvement(.*)?", "unknown", clean)
        clean = re.sub(r"(.*)?m?shark(.*)?", "unknown", clean)
        clean = re.sub(r"(.*)?invalid?(.*)?", "unknown", clean)
        clean = re.sub(r"(.*)?questionable(.*)?", "unknown", clean)
        clean = re.sub(r"(.*)?unidentified(.*)?", "unknown", clean)
        clean = re.sub(r"(.*)?possibly(.*)?", "unknown", clean)
        clean = re.sub(r"(.*)?(\.)(.*)?", "unknown", clean)
        clean = re.sub(r"(.*)?dooley(.*)?", "unknown", clean)
        clean = re.sub(r"(.*)?doubtful(.*)?", "unknown", clean)
        clean = re.sub(r"(.*)?\sto\s(.*)?", "unknown", clean)
        clean = re.sub(r"(.*)?5(.*)?", "unknown", clean)
        clean = re.sub(r"(.*)?\s(.*)?", "unknown", clean)
    
        clean_species.append(clean)
    
    return clean_species


def find_sharks(data):
    shark = []
    for s in data:
        types = "".join(re.findall(r"\w*\s\bshark",s))
        if types == "":
            types = "unknown"
        print(types)
        shark.append(types)
    return shark


def find_year(data):
    year = []
    for v in data:
        reg = "".join(re.findall(r"\d{4}",v))

        if reg == "":
            reg = np.nan

        year.append(reg)
    return year


def find_month(data):
    month = []
    for v in data:
        reg = "".join(re.findall(r"\-[A-z]{3}\-",v))
        reg = re.sub(r"\-","",reg)

        if reg == "":
            reg = np.nan

        month.append(reg)
    return month
    

def clean_cols(df):
    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.replace(r"\."," ")
    df.columns = df.columns.str.replace(r"\s$","")
    df.columns
    return df.columns
import re

def shark_species(data):
    clean_species = []

    for s in data:

        clean = re.sub(r"\.*?whitetip\.*?", "whitetip", data)
        clean = re.sub(r"\.*?tiger\.*?", "tiger", data)
        clean = re.sub(r"\.*?bull\.*?", "bull", data)
        clean = re.sub(r"\.*?nurse\.*?", "nurse", data)
        clean = re.sub(r"\.*?whaler\.*?", "whaler", data)
        clean = re.sub(r"\.*?blacktip\.*?", "blacktip", data)
        clean = re.sub(r"\.*?reef\.*?", "reef", data)
        clean = re.sub(r"\.*?mako\.*?", "mako", data)
        clean = re.sub(r"\.*?raggedtooth\.*?", "raggedtooth", data)
        clean = re.sub(r"\.*?wobbegong\.*?", "wobbegong", data)
        clean = re.sub(r"\.*?spinner\.*?", "spinner", data)
        clean = re.sub(r"\.*?hammerhead\.*?", "hammerhead", data)
        clean = re.sub(r"\.*?blue\.*?", "blue", data)
        clean = re.sub(r"\.*?lemon\.*?", "lemon", data)
        clean = re.sub(r"\.*?zambesi\.*?", "zambesi", data)
        clean = re.sub(r"\.*?sandtiger\.*?", "sandtiger", data)
        clean = re.sub(r"\.*?sandbar\.*?", "sandbar", data)
        clean = re.sub(r"\.*?sevengill\.*?", "sevengill", data)
        clean = re.sub(r"\.*?dusky\.*?", "dusky", data)
        clean = re.sub(r"\.*?carpet\.*?", "carpet", data)
        clean = re.sub(r"\.*?angel\.*?", "angel", data)
        clean = re.sub(r"\.*?galapagos\.*?", "galapagos", data)
        clean = re.sub(r"\.*?basking\.*?", "basking", data)
        clean = re.sub(r"\.*?gill\.*?", "gill", data)
        clean = re.sub(r"\.*?porbeagle\.*?", "porbeagle", data)
        clean = re.sub(r"\.*?copper\.*?", "copper", data)
        clean = re.sub(r"\.*?colored\.*?", "colored", data)
        clean = re.sub(r"\.*?dog\.*?", "dog", data)
        clean = re.sub(r"\.*?silky\.*?", "silky", data)
        clean = re.sub(r"\.*?white\.*?", "white", data)
        clean = re.sub(r"\.*?sand\.*?", "sand", data)
        clean = re.sub(r"\.*?zambezi\.*?", "zambezi", data)
        clean = re.sub(r"\.*?thresher\.*?", "thresher", data)
        clean = re.sub(r"\.*?salmon\.*?", "salmon", data)
        clean = re.sub(r"\.*?", "unknown", data)
    
        clean_species.append(clean)
    
    return clean_species
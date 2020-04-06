import pandas as pd
import numpy as np
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


def clean_type(df):
    df.type = df.type.fillna("invalid")
    df.type = df.type.str.lower()
    df.type = df.type.str.replace("questionable", "invalid")
    df.loc[df.type.str.startswith("boat"), "type"] = "boat"
    return df.type


def clean_country(df):
    df.country = df.country.fillna("no country")
    df.country = df.country.str.lower()
    df.country = df.country.str.replace("england", "united kingdom")
    df.country = df.country.str.replace("scotland", "united kingdom")
    df.country = df.country.str.replace(r"(.*)?ocean(.*)?", "no country")
    df.country = df.country.str.replace(r"(.*)?sea(.*)?", "no country")
    return df.country


def clean_activity(df):
    df.activity = df.activity.fillna("unknown")
    df.activity = df.activity.str.lower()
    df.activity = df.activity.str.replace(r"(.*)?surf(.*)?",("surfing"))
    df.activity = df.activity.str.replace(r"(.*)?swim(.*)?",("swimming"))
    df.activity = df.activity.str.replace(r"(.*)?diving(.*)?",("diving"))
    df.activity = df.activity.str.replace(r"(.*)?paddl(.*)?",("paddle"))
    df.activity = df.activity.str.replace(r"(.*)?fish(.*)?",("fishing"))
    df.activity = df.activity.str.replace(r"(.*)?boat(.*)?",("boat"))
    df.activity = df.activity.str.replace(r"(.*)?float(.*)?",("floating"))
    return df.activity


def clean_sex(df):    
    df.sex = df.sex.fillna("NA")
    df.sex = df.sex.str.replace(r"(.*)?M(.*)?","M")
    df.sex = df.sex.str.replace(r"(.*)?N(.*)?","NA")
    df.sex = df.sex.str.replace(".","NA")
    df.sex = df.sex.str.replace("lli","NA")
    return df.sex


def clean_age(df):
    df.age = df.age.str.replace(r"\b[^\d\W]+\b","0")
    df.age = df.age.str.replace(r"\s+","0")
    df.age = df.age.str.replace(r"½","0")
    df.age = df.age.str.replace(r">5","6")
    df.age = df.age.str.replace(r"?","0")
    df.age = df.age.str.replace(r"(","0")
    df.age = df.age.str.replace(r'"',"0")
    df.age = pd.to_numeric(df.age, downcast='signed')
    return df.age
    

def clean_fatal(df):
    df["fatal (y/n)"] = df["fatal (y/n)"].fillna("UNKNOWN")
    df["fatal (y/n)"] = df["fatal (y/n)"].str.replace(r"\s+N","N")
    df["fatal (y/n)"] = df["fatal (y/n)"].str.replace(r"(.*)?M(.*)?","N")
    df["fatal (y/n)"] = df["fatal (y/n)"].str.replace(r"2017","UNKNOWN")
    return df["fatal (y/n)"]
from datetime import date

def gen_birth_date(season, age):

    current_year = date.today().year
    birth_year = current_year - int(age)
    season_dates = {
        "spring": "-03-21",
        "summer": "-06-21",
        "fall": "-09-21",
        "winter": "-12-21"
    }

    season = season.lower().strip() if season else "unknown"
    return f"{birth_year}{season_dates.get(season, '-06-21')}"

def gen_unique_id(species, number):
    code = species[:2].capitalize()
    return f"{code}{number:02d}"

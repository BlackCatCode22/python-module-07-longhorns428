# main.py
import re
from datetime import date
from hyena import Hyena
from lion import Lion
from tiger import Tiger
from bear import Bear

def parse_animal_line(line):
    pattern = r"(\d+)\s+year old\s+(\w+)\s+(\w+), born in\s+(\w+|unknown)[,]?\s*([\w\s\-]+)\s+color,\s+(\d+)\s+pounds,\s+from\s+(.+)"
    match = re.match(pattern, line.strip(), re.IGNORECASE)
    if match:
        age, sex, species, season, color, weight, origin = match.groups()
        return age, sex, species.capitalize(), season.strip(), color.strip(), weight.strip(), origin.strip()
    else:
        print(f"⚠️ Could not parse: {line}")
        return None

def load_animal_names(filename):
    """Load animal names grouped by species headers."""
    sections = {"Hyena": [], "Lion": [], "Tiger": [], "Bear": []}
    current_species = None
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if "hyena" in line.lower():
                current_species = "Hyena"
            elif "lion" in line.lower():
                current_species = "Lion"
            elif "tiger" in line.lower():
                current_species = "Tiger"
            elif "bear" in line.lower():
                current_species = "Bear"
            elif current_species:
                # Split comma-separated names, clean extra spaces
                names = [n.strip() for n in line.split(",") if n.strip()]
                sections[current_species].extend(names)
    return sections

def main():
    with open("arrivingAnimals.txt", "r", encoding="utf-8") as f:
        animals = [line.strip() for line in f if line.strip()]

    names_by_species = load_animal_names("animalNames.txt")

    zoo = {"Bear": [], "Hyena": [], "Lion": [], "Tiger": []}
    counters = {s: 1 for s in zoo.keys()}
    name_indexes = {s: 0 for s in zoo.keys()}

    for line in animals:
        parsed = parse_animal_line(line)
        if not parsed:
            continue
        age, sex, species, season, color, weight, origin = parsed
        if species not in zoo:
            print(f"⚠️ Unknown species: {species}")
            continue

        species_names = names_by_species.get(species, [])
        idx = name_indexes[species]
        if idx < len(species_names):
            name = species_names[idx]
            name_indexes[species] += 1
        else:
            name = f"Unnamed-{species}"

        if species == "Hyena":
            zoo["Hyena"].append(Hyena(name, age, sex, season, color, weight, origin, counters["Hyena"]))
        elif species == "Lion":
            zoo["Lion"].append(Lion(name, age, sex, season, color, weight, origin, counters["Lion"]))
        elif species == "Tiger":
            zoo["Tiger"].append(Tiger(name, age, sex, season, color, weight, origin, counters["Tiger"]))
        elif species == "Bear":
            zoo["Bear"].append(Bear(name, age, sex, season, color, weight, origin, counters["Bear"]))

        counters[species] += 1

    today = date.today().isoformat()
    total_animals = 0
    with open("zooPopulation.txt", "w", encoding="utf-8") as out:
        out.write(f"Zoo Population Report — Generated on {today}\n")
        out.write("=" * 60 + "\n\n")

        for species in sorted(zoo.keys()):
            animals = zoo[species]
            if not animals:
                continue
            sound = animals[0].sound
            out.write(f"=== {species} Habitat ===\n")
            out.write(f"Sound: {sound}\n\n")
            for animal in animals:
                out.write(str(animal) + "\n")
            out.write("\n")
            total_animals += len(animals)

        out.write("=== Zoo Summary ===\n")
        for species in sorted(zoo.keys()):
            out.write(f"{species}: {len(zoo[species])} animals\n")
        out.write(f"\nTotal animals: {total_animals}\n")

    print("✅ zooPopulation.txt has been fixed and regenerated correctly!")

if __name__ == "__main__":
    main()

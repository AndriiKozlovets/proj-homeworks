class Country:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def add(self, other_country):
        new_name = f'{self.name} {other_country.name}'
        new_population = self.population + other_country.population
        return Country(new_name, new_population)


# Example usage:
bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

bosnia_herzegovina = bosnia.add(herzegovina)
print(bosnia_herzegovina.population)  # Output: 15000000
print(bosnia_herzegovina.name)        # Output: 'Bosnia Herzegovina'

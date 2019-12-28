from population import evolve, random_population, inject_archetypes

POPULATION = random_population(size=100, n_genes=10, gene_sum=100)
POPULATION = inject_archetypes(POPULATION)
GENERATIONS = 1000

EVOLVED_POPULATION = evolve(POPULATION, GENERATIONS)

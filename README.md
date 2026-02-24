# N-Queens Problem: Comparative Study of Four Algorithms

This project presents a systematic implementation and empirical comparison of four classical search and metaheuristic optimization algorithms applied to the N-Queens problem.

The study evaluates scalability, execution time, memory consumption, convergence behavior, and solution capability across increasing board sizes (N = 10, 30, 50, 100, 200).

---

## Table of Contents

- [Problem Overview](#problem-overview)
- [Implemented Algorithms](#implemented-algorithms)
- [Experimental Setup](#experimental-setup)
- [Algorithm Parameter Configuration](#algorithm-parameter-configuration)
- [Performance Summary](#performance-summary)
- [Relevance to Optimization and Artificial Intelligence](#relevance-to-optimization-and-artificial-intelligence)
- [Repository Structure](#repository-structure)
- [Future Work](#future-work)
- [Academic Context](#academic-context)
- [License](#license)
  
---

## Problem Overview

The N-Queens problem requires placing N queens on an N×N chessboard such that no two queens attack each other horizontally, vertically, or diagonally.

As N increases, the search space grows combinatorially, making the problem an effective benchmark for analyzing:

Search complexity

Optimization landscapes

Local vs global minima behavior

Scalability under constrained resources

This makes it particularly relevant for understanding algorithmic optimization strategies used in AI systems.

---



## Implemented Algorithms

### Exhaustive Search (DFS with Backtracking)

Exhaustive Search explores the entire solution space using a depth-first traversal strategy combined with backtracking.  
At each column, the algorithm attempts to place a queen in every possible row and recursively proceeds to the next column.  
If a conflict is detected, it backtracks to the previous state and tries an alternative placement.

**Key Characteristics:**

* Performs a complete and systematic exploration of the search space  
* Guarantees finding a valid solution (if one exists)  
* Deterministic and exact  
* Time complexity grows exponentially with N  
* Memory usage increases rapidly due to recursive state tracking  
* Practical only for small board sizes (typically N ≤ 15–20)

While theoretically sound and guaranteed, DFS becomes computationally infeasible as the problem size increases.


### Greedy Search (Hill Climbing with Enhancements)

Greedy Search applies the minimum-conflicts heuristic by iteratively improving the current board configuration.  
Starting from a randomized initialization (one queen per column), the algorithm moves queens to positions that minimize conflicts.

To reduce stagnation, two enhancements were introduced:

- **Max Restarts:** Reinitialize the board when trapped in local minima  
- **Sideways Move Probability:** Allow equal-conflict moves to escape flat regions  

**Key Characteristics:**

* Fast local search mechanism  
* Low memory consumption  
* Effective for small-to-medium board sizes 
* Performance highly dependent on restart strategy  
* Susceptible to local optima in large search spaces  

Hill Climbing performs efficiently under moderate constraints but lacks robustness when the landscape becomes highly complex.



### Simulated Annealing

Simulated Annealing is a accidental metaheuristic inspired by the physical annealing process in metallurgy.  
Unlike greedy approaches, it occasionally accepts worse solutions based on a temperature-controlled probability, enabling broader exploration.

The algorithm is taken over:

- **Initial Temperature**
- **Cooling Schedule**
- **Maximum Steps**

Higher temperatures allow exploration, while gradual cooling increases exploitation.

**Key Characteristics:**

* Probabilistic exploration strategy  
* Capable of escaping local minima  
* Strong scalability up to N = 100 in experiments  
* Stable memory consumption  
* Performance sensitive to parameter tuning  

Simulated Annealing provides a strong balance between exploration and convergence, making it one of the most scalable approaches in this study.


### Genetic Algorithm (Evolutionary Optimization)

The Genetic Algorithm (GA) is a population-based evolutionary optimization method inspired by natural selection.  
Instead of exploring a single solution, GA evolves a population of candidate solutions across generations.

Core mechanisms include:

- **Tournament Selection (k-selection)**  
- **Crossover (recombination)**  
- **Mutation (random perturbation)**  
- **Elitism (preserving top individuals)**  
- **Stagnation Threshold Reset**  
- **Hybrid Local Search Refinement**

**Key Characteristics:**

* Global search capability  
* Suitable for large and complex search spaces  
* Flexible and adaptable via parameter tuning  
* Computationally intensive  
* High memory consumption due to population storage  

Genetic Algorithms demonstrate strong exploratory power but require significant computational resources, especially as N increases.

---

## Experimental Setup

All experiments were executed under identical hardware and software conditions:

| Component | Specification      |
| --------- | ------------------ |
| CPU       | Apple M1 Pro       |
| RAM       | 16 GB              |
| OS        | macOS              |
| Language  | Python 3.10        |
| IDE       | Visual Studio Code |

Each algorithm was executed three times for each board size to ensure consistency and reliability of the measurements.


---

## Algorithm Parameter Configuration

Below are the parameter values used during experimentation across different board sizes.


### Exhaustive Search (DFS)

DFS does not require tunable hyperparameters.

- Deterministic backtracking search
- Explores all possible placements
- No probabilistic components

---

### Greedy Search (Hill Climbing)

| N   | Max Restarts | Sideways Move Probability |
|-----|-------------|--------------------------|
| 10  | 20          | 0.3                      |
| 30  | 20          | 0.3                      |
| 50  | 20          | 0.3                      |
| 100 | 50          | 0.4                      |
| 200 | 50          | 0.4                      |

**Parameter Ranges Explored:**
- Max Restarts: 20 – 50
- Sideways Probability: 0.2 – 0.5

These parameters were introduced to reduce the probability of getting trapped in local minima.

---

### Simulated Annealing

| N   | Max Steps | Start Temperature | Cooling Rate |
|-----|-----------|------------------|--------------|
| 10  | 2,000     | 2.0              | 0.99         |
| 30  | 10,000    | 2.0              | 0.99         |
| 50  | 50,000    | 10.0             | 0.995        |
| 100 | 100,000   | 20.0             | 0.999        |
| 200 | 1,000,000 | 40.0             | 0.9995       |

**Parameter Ranges Explored:**
- Max Steps: 1,000 – 2,000,000
- Start Temperature: 1.0 – 60.0
- Cooling Rate: 0.90 – 0.9999

Higher N values required:
- Larger search budgets
- Higher initial temperatures
- Slower cooling schedules

### Genetic Algorithm

| N   | Pop Size | Generations | p_crossover | p_mutation | k | Elitism | Stagnation | Local Search Steps |
|-----|----------|-------------|-------------|------------|---|----------|-------------|--------------------|
| 10  | 40       | 100         | 0.85        | 0.18       | 3 | 2        | 10          | 2                  |
| 30  | 80       | 160         | 0.93        | 0.14       | 4 | 2        | 15          | 2                  |
| 50  | 100      | 200         | 0.80        | 0.10       | 3 | 2        | 50          | 1                  |
| 100 | 600      | 1200        | 0.92        | 0.17       | 5 | 2        | 70          | 2                  |
| 200 | 2000     | 1200        | 0.90        | 0.18       | 6 | 6        | 120         | 10                 |

**Parameter Ranges Explored:**
- Population Size: 30 – 3000
- Generations: 90 – 1500
- p_crossover: 0.80 – 0.99
- p_mutation: 0.10 – 0.30
- k (Tournament size): 2 – 8
- Elitism: 2 – 6
- Stagnation Threshold: 10 – 120
- Local Search Steps: 1 – 12

Genetic Algorithm performance was highly sensitive to parameter tuning, especially for larger board sizes.


---

## Performance Summary

### Small N (N ≤ 30)
* All algorithms perform efficiently
* DFS is fastest but memory-heavy

### Medium N (N ≤ 50)
* Greedy and Simulated Annealing perform well
* GA starts becoming computationally expensive

### Large N (N ≤ 100)
* Simulated Annealing and GA successfully find solutions
* SA shows better time-memory tradeoff

### Very Large N (N = 200)
* No algorithm reached a valid solution under tested constraints
* Requires further tuning and hybrid strategies and more resources


### Key Observations

* DFS is not scalable beyond small boards.
* Greedy Search struggles with local optima for large N.
* Simulated Annealing provides the best balance between memory and scalability.
* Genetic Algorithm is powerful but resource-intensive.

---

## Relevance to Optimization and Artificial Intelligence

Although the N-Queens problem is a classical combinatorial optimization challenge, the implemented approaches are strongly connected to optimization principles widely used in artificial intelligence and machine learning.

- **Simulated Annealing** reflects stochastic optimization behavior similar to exploration mechanisms in machine learning training, where controlled randomness helps avoid premature convergence to poor local minima.

- **Genetic Algorithms** belong to evolutionary computation and are commonly applied in hyperparameter optimization, neural architecture search, and global optimization tasks in AI systems.

- **Hill Climbing (Greedy Search)** demonstrates local search dynamics analogous to gradient-based optimization methods, where iterative improvements are made toward minimizing an objective function.

- The study emphasizes core optimization concepts such as:
  - Local vs global minima
  - Convergence behavior
  - Exploration–exploitation trade-offs
  - Search landscape complexity
  - Scalability under resource constraints

Understanding these dynamics strengthens foundational knowledge in optimization-driven AI systems and provides insight into how complex models are trained and tuned in modern machine learning pipelines.
---

## Repository Structure

```
N-Queens/
│
├── dfs.py
├── greedy.py
├── simulated_annealing.py
├── genetic_algorithm.py
├── experiments/
└── results/
```

---

## Future Work

- [ ] Hybrid Genetic Algorithm + Local Search integration
- [ ] Adaptive cooling schedules in Simulated Annealing
- [ ] Parallel or distributed implementations
- [ ] Automated hyperparameter tuning
- [ ] Scaling experiments beyond N = 200

---

## Academic Context

This project was developed as part of an academic study in combinatorial optimization and algorithm analysis, with emphasis on empirical benchmarking, parameter sensitivity, and scalability evaluation.

---

## License

MIT License

# Project_Pokemon

## Problem Statement

**The goal of the project is to gather information about the best Pokémon in terms of their attack, defense, and speed, while also determining which types of Pokémon perform better. Additionally, I will scrape data from the [website](https://pokemondb.net/pokedex/all) to achieve this objective.**

**1.Which Pokémon has the highest Attack stat, and what is its type?**

**2.How does the Speed distribution vary among different Pokémon types, as shown in the area plot?**

**3.Which Pokémon has the highest Defense stat and what is its type?**

**4.How does the average HP of Pokémon vary across different types as shown in the line plot?**

**5.What is the distribution of Pokémon types in this dataset and which type has the minimum attack?**

**6.What are the Special Attack (Sp. Atk) stats for each Pokémon type and which type has the highest Special Attack?**

**7.What are the Special Defense (Sp. Def) stats for each Pokémon type and which type has the highest Special Defense?**

You can visit the public Dashboard [here](https://public.tableau.com/app/profile/sadikal.jarif/viz/FinalProject_Pokemon_Update/Dashboard2)

# Findings and Observations from the Dashboard :

**1.Mega Mewtwo X: Psychic type with max attack of 190.**

**2.Water type: 5602 defense.**

**3.Eternatus Eternamax: Poison/Dragon type with 250 max defense.**

**4.Dark Ground type: Average HP of 155.**

**5.Happiny (Normal type): Min attack 5. Chansey (Normal type): Min attack 5.**

**6.Mega Mewtwo Y: Psychic type, max Special Attack 194.**

**7.Eternatus Eternamax: Poison/Dragon type, Special Defense 250.**

### Build from sources and run the Selenium Scraper
**1.Clone the repository:**
>git clone https://github.com/jarif87/Project_Pokemon/tree/main.git

**2.Initialize and active Virtual Environment:**
>virtualenv venv

>.\venv\Scripts\activate

**3.Install dependencies:**
>pip install -r requirements.txt

**4.Run the scrape:**
>python Project_Pokemon/Pokemon.py

**5.You will receive a file named **"Pokemon.csv"** which contains all the required fields. Alternatively, you can review our scraped data by checking it [here](https://github.com/jarif87/Project_Pokemon/blob/main/Pokemon.csv)**


![](https://public.tableau.com/static/images/Bo/Book10_17002239230480/Type_And_Speed/4_3.png)

![](https://public.tableau.com/static/images/Bo/Book11_17002247483220/Name_and_attack/4_3.png)

![](https://public.tableau.com/static/images/Bo/Book13_17002258479330/typehpaverage/4_3.png)

![](https://public.tableau.com/static/images/Bo/Book19_17003109802900/Sheet9/4_3.png)

![](https://public.tableau.com/static/images/Bo/Book18_17003106062660/Sheet8/4_3.png)




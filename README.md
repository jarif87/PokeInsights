# PokéInsights

## Problem Statement

**The goal of the project is to gather information about the best Pokémon in terms of their attack, defense, and speed, while also determining which types of Pokémon perform better. Additionally, I will scrape data from the [website](https://pokemondb.net/pokedex/all) to achieve this objective.**

**1. Which Pokémon has the highest Attack stat, and what is its type?**

**2. How does the Speed distribution vary among different Pokémon types, as shown in the area plot?**

**3. Which Pokémon has the highest Defense stat and what is its type?**

**4.How does the average HP of Pokémon vary across different types as shown in the line plot?**

**5. What is the distribution of Pokémon types in this dataset and which type has the minimum attack?**

**6. What are the Special Attack (Sp. Atk) stats for each Pokémon type and which type has the highest Special Attack?**

**7. What are the Special Defense (Sp. Def) stats for each Pokémon type and which type has the highest Special Defense?**

You can visit the public Dashboard here  [Dashboard_1](https://public.tableau.com/app/profile/sadikal.jarif/viz/MyFinalDashboard_1/Dashboard1) and [Dashboard_2](https://public.tableau.com/app/profile/sadikal.jarif/viz/MyFinalDashboard_2/Dashboard2)

# Findings and Observations from the Dashboard :

**1. Mega Mewtwo X has the highest Attack stat, with a type of Psychic.**

**2. The area plot displays the Speed distribution across various Pokémon types, providing insights into how different types compare in terms of speed.**

**3. Eternatus Eternamax holds the highest Defense stat, belonging to the Poison/Dragon type.**

**4. The line plot illustrates the average HP of Pokémon across different types, offering a visual representation of the variations in HP among various Pokémon types.**

**5. The dataset showcases the distribution of Pokémon types, highlighting the type with the minimum attack as Happiny (Normal type) and Chansey (Normal type), both having a minimum attack of 5.**

**6. Mega Mewtwo Y boasts the highest Special Attack stat among Pokémon types, specifically in the Psychic category, with a max Special Attack of 194.**

**7. Eternatus Eternamax, a Poison/Dragon type, showcases the highest Special Defense stat, reaching a value of 250. The Special Defense stats for each Pokémon type can be explored through the provided data and visualizations.**

### Build from sources and run the Selenium Scraper
**1.Clone the repository:**
>git clone https://github.com/jarif87/Project_Pokemon/tree/main.git

**2.Initialize and active Virtual Environment:**
>virtualenv venv

>.\venv\Scripts\activate

**3.Install dependencies:**
>pip install -r requirements.txt

**4.Run the scrape:**
>python Project_Pokemon/WebScraping/scraper.py

**5.You will receive a file named **"Pokemon.csv"** which contains all the required fields. Alternatively, you can review our scraped data by checking it [here](https://github.com/jarif87/Project_Pokemon/blob/main/Data/Pokemon.csv)**

# Findings  from the Dashboard :

**1. Mega Mewtwo X has the highest Attack stat, with a type of Psychic.**

![](https://public.tableau.com/static/images/My/MyBook_1_17034186031370/NameAndAttack/4_3.png)

**2. The area plot displays the Speed distribution across various Pokémon types, providing insights into how different types compare in terms of speed.**
   
![](https://public.tableau.com/static/images/My/MyBook_2_17034186348710/TypeAndSpeed/4_3.png)

**3. Eternatus Eternamax holds the highest Defense stat, belonging to the Poison/Dragon type.**
   
![](https://public.tableau.com/static/images/My/MyBook_3_17034186970480/NameAndDefence/4_3.png)

**4. The line plot illustrates the average HP of Pokémon across different types, offering a visual representation of the variations in HP among various Pokémon types.**
   
![](https://public.tableau.com/static/images/My/MyBook_4_17034187611130/TypeAndAverageHP/4_3.png)

**5. The dataset showcases the distribution of Pokémon types, highlighting the type with the minimum attack as Happiny (Normal type) and Chansey (Normal type), both having a minimum attack of 5.**
   
![](https://public.tableau.com/static/images/My/MyBook_5_17034188051970/NameTypeAndMinimumAttack/4_3.png)

**6. Mega Mewtwo Y boasts the highest Special Attack stat among Pokémon types, specifically in the Psychic category, with a max Special Attack of 194.**
   
![](https://public.tableau.com/static/images/My/MyBook_6_17034188801390/NameTypeAndMaxSpecialAttack/4_3.png)

**7. Eternatus Eternamax, a Poison/Dragon type, showcases the highest Special Defense stat, reaching a value of 250. The Special Defense stats for each Pokémon type can be explored through the provided data and visualizations.**
   
![](https://public.tableau.com/static/images/My/MyBook_7_17034189683050/NameTypeAndSpecialMaxDefence/4_3.png)



# Features 
----

## Home Page


The Home Page serves as the main entry point to the Art Color Picker web application. It provides easy navigation to key features:


- About: A link directing users to the About Page, where they can learn more about the application.

- Color Picker: A link leading to the Colors Page, where users can explore and select colors.


---

## Pages Header


Each Page contains a header menu with a search bar, drop-down menu and multiple navigation links. 


### Multiple navigation links: 


- ART COLOR PICKER: A clickable text link that redirects users back to the Home Page.

- PALLETES: A link to the Palettes Page, where color combinations are displayed in an organized manner, following the structure of a reference book.

- RANDOM: A link that generates three random palettes. Each click on the "Random" link generates a new set of palettes:

        - One palette with 2 colors
        - One palette with 3 colors
        - One palette with 4 colors

- COLORS: A link to the Colors Page, where colors are categorized by groups.
  


### Search Bar


The search bar allows users to enter a maximum of 9 characters, including only the "#" symbol, numbers (0-9), letters (a-z, A-Z). Any other characters are not accepted. 

The program processes the input by removing the "#" symbol and converting it into an RGB format to: 

        - Retrieve matching colors from the database
        - Suggest similar colors if the exact match is unavailable, allowing users to select from existing color options in the database.



### Drop-down Menu


A drop-down menu provides additional navigation options and user preferences.

----

## About Page

The About Page provides an overview of the Art Color Picker application, explaining its purpose, features, and how users can interact with it.


----

## Colors Page

The Colors Page displays color options in a grid layout with interactive elements:

    - Color Squares (Buttons): Clicking a color square connects to the database and opens the Palettes Page, filtering palettes that contain the selected color.

    - Heart Button: Saves the selected color to the user's collection of favorite choices.

    - Sakura Button: Opens filter options to filter by color category.

    

----

## Palettes Page

The Palettes Page presents curated color combinations sourced from the database. The display order follows a structured format inspired by a reference book. Users can access palettes in two ways:

    - Directly from the Palettes Page, where all available combinations are shown.

    - Through the Colors Page or Random feature, where palettes containing specific colors or randomly selected combinations are displayed.


----

## Interactive Features

Heart Button: Saves a color combination to the user's personal collection.

Desk Button: Opens the selected palette on a full screen.

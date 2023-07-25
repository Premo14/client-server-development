# client-server-development
Client/Server Development Course - CS340

Anthony Premo 

 

# Project Two: Grazioso Salvare Dashboard - README 

  

## Overview 

  

This project involves the development of a web application dashboard for Grazioso Salvare, an innovative international rescue-animal training company. The dashboard will interact with a MongoDB database and allow users to identify and categorize dogs for search-and-rescue training based on certain profiles. The dashboard will include interactive options to filter data, an interactive data table, and dynamic charts. Additionally, the dashboard will display a geolocation chart and the user's unique identifier. 

  

## Required Functionality 

  

The dashboard will provide the following required functionalities: 

  

1. Interactive options to filter the Austin Animal Center Outcomes data set. 

2. An interactive data table that displays an unfiltered view of the data set. 

3. Charts, including a geolocation chart and a second chart, that dynamically respond to filtering options. 

4. Display of the Grazioso Salvare logo and the developer's unique identifier. 

  
  

To demonstrate the dashboard's functionality, the following screenshots were taken: 

  

1. Starting state of the dashboard: Includes interactive options for data filtering, an interactive data table, and charts. 

2. Dashboard after applying the "Water Rescue" filter. 

3. Dashboard after applying the "Mountain or Wilderness Rescue" filter. 

4. Dashboard after applying the "Disaster or Individual Tracking" filter. 

5. Dashboard in its original, unfiltered state after applying the "Reset" filter. 

  

## Tools Used 

  

The following tools were used to achieve the dashboard functionality: 

  

1. MongoDB: Used as the model component of the development due to its flexibility, scalability, and compatibility with Python through the PyMongo library. 

  

2. Dash Framework: Provides the view and controller structure for the web application, allowing the creation of interactive and user-friendly dashboards. 

  

## Steps Taken to Complete the Project 

  

1. Developed a MongoDB database and established CRUD routines in Python for MongoDB as part of Project One. 

  

2. Created a data table on the dashboard that shows an unfiltered view of the Austin Animal Center Outcomes data set. Retrieved data from MongoDB using the previous CRUD Python module. 

  

3. Developed database queries that match the required filter functionality to properly retrieve data from the database. 

  

4. Developed interactive options, such as radio items and drop-down menus, to allow users to select data based on filtering functions. 

  

5. Modified the data table to be interactive and respond to input from the interactive options. 

  

6. Created charts, including a geolocation chart and a second chart, that display data in response to updates from the data table. 

  

7. Tested and deployed the dashboard to ensure all components work as expected. 

  

## Challenges and Overcoming Them 

  

One of the challenges encountered was ensuring smooth communication between the dashboard widgets and the MongoDB database. This challenge was overcome by properly implementing the CRUD Python module, which provided a standardized interface for interacting with the database. 

  

## Conclusion 

  

The Grazioso Salvare dashboard provides a user-friendly and intuitive interface for identifying and categorizing dogs for search-and-rescue training. With interactive options, a dynamic data table, and responsive charts, users can efficiently analyze and visualize data from the animal shelters. The open-source nature of the code on GitHub allows similar organizations to benefit from and adapt the dashboard to their specific needs. 

  

--- 

  

Screenshots: 

 

 

 

Questions: 

 

1. Writing maintainable, readable, and adaptable programs is essential for efficient software development. In the case of the CRUD Python module from Project One, I followed some best practices to achieve these goals: 

  

   - **Modularization:** I designed the CRUD module to be modular, with separate functions for each CRUD operation. This makes it easier to maintain and update specific functionalities without affecting other parts of the code. 

  

   - **Code Documentation:** I provided clear comments and documentation within the CRUD module to explain the purpose and usage of each function. This helps other developers (or even my future self) understand the code without diving into its implementation details. 

  

   - **Consistent Naming and Formatting:** I followed a consistent naming convention and code formatting throughout the module. This promotes readability and makes it easier to understand the code's structure. 

  

   - **Error Handling:** I included error handling mechanisms in the module to gracefully handle exceptions and provide informative error messages. This aids in debugging and ensures that the program can handle unexpected scenarios. 

  

   - **Parameterization:** I made the module more adaptable by using parameters for host, port, username, password, etc. This allows the module to be easily reused with different database configurations. 

  

   The advantage of working with a well-structured CRUD module is that it provides a reusable, standardized interface for interacting with a database. By using this module in Project Two's dashboard, I could easily connect to the MongoDB database, retrieve data, and display it in the dashboard components. This saved time and effort compared to rewriting the database access code for each dashboard widget. 

  

   In the future, I could use the CRUD module for other projects that involve database interactions. Whether it's creating new dashboards, web applications, or data analysis tasks, having a modular CRUD module will simplify and expedite the process of working with databases. 

  

2. As a computer scientist, I approach a problem by first understanding the requirements and constraints. For the database and dashboard requirements from Grazioso Salvare, I carefully reviewed the prompt and determined what functionalities needed to be implemented. 

  

   My approach for this project differed from some previous assignments in other courses because it involved integrating different components (dashboard widgets and the database) and considering user interaction. Instead of focusing solely on algorithms and data structures, I had to design a user-friendly dashboard and ensure smooth communication with the database. 

  

   To create databases for future client requests, I would: 

  

   - **Client Consultation:** I would start by having detailed discussions with the client to understand their specific needs, data structure, and access requirements. 

  

   - **Data Modeling:** I would create a well-designed data model that accurately represents the client's data and allows for efficient data retrieval and storage. 

  

   - **Scalability:** I would consider scalability options, such as sharding or replication, depending on the anticipated data growth. 

  

   - **Security:** Ensuring the security of the database is crucial, so I would implement appropriate access controls, encryption, and other security measures. 

  

   - **Testing and Optimization:** Before deploying the database, I would thoroughly test its performance and optimize it to ensure it meets the client's performance expectations. 

  

3. Computer scientists are professionals who study and develop algorithms, data structures, and computational systems to solve complex problems and improve various aspects of life. In the context of this project, the work on the database and dashboard helps Grazioso Salvare by providing a user-friendly dashboard to visualize and analyze their animal outcomes data efficiently. 

  

   Specifically, the dashboard can: 

  

   - **Facilitate Decision-Making:** The dashboard presents data in a visually appealing manner, enabling quick insights into animal outcomes. Grazioso Salvare staff can make informed decisions based on real-time data. 

  

   - **Increase Efficiency:** By integrating the CRUD Python module with the dashboard, the company can seamlessly access the MongoDB database without the need for manual database queries. This automation streamlines their data retrieval process. 

  

   - **Improve Data Visibility:** The geolocation chart allows Grazioso Salvare to visualize the location of animals, helping them track trends and plan resources accordingly. 

  

   - **Enhance Communication:** The dashboard can be shared with stakeholders, enabling transparent communication about animal outcomes and shelter operations. 

  

   Ultimately, the work on this project helps Grazioso Salvare better manage their animal outcomes data and optimize their processes, ultimately improving their overall efficiency and effectiveness as an organization. 

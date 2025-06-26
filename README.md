# CS-340-Final-Project-Grazioso-Salvare-Rescue-Dashboard
This repo contains the final project for CS-340: a full-stack dashboard created to help Grazioso Salvare identify dogs suited for rescue missions. The app is built using Python with the Dash framework and MongoDB as the backend. The dashboard features filtering widgets, an interactive data table, a geolocation map, and a secondary chart—all wired through a custom CRUD module written in Project One.

## Project Reflection
### Writing Maintainable, Readable, and Adaptable Code
The AnimalShelter module I built earlier played a big role here. By keeping the core database operations (create, read, update, delete) in one place, the rest of the dashboard stayed clean and modular. I didn’t have to rewrite any DB logic—just passed filters to the read function. That structure made it much easier to plug the module into Dash and test things quickly. It’s also flexible enough to reuse for other projects like Flask APIs or even testing scripts.

## My Approach to Solving Problems
I usually start by identifying what the client wants, then breaking those down into smaller tasks. For this dashboard, I focused first on reading and filtering data correctly before layering on the UI parts. One of the trickier parts was keeping the filters consistent and ensuring multiple filters work together as “AND” conditions. I also made sure to test each step visually using the Dash layout. Compared to previous assignments, this one was more like a real-world client project, and I approached it that way—figuring out user needs, iterating, and testing often.

## What Computer Scientists Do and Why It Matters
Projects like this show how software can support real-world work. For Grazioso Salvare, being able to filter animals by traits like breed, outcome, and age helps them make decisions quickly. It saves time and improves the quality of rescue assignments. That’s what computer scientists do. We build tools to make things easier, faster, or more effective. The value shows up when others can use what we build to do their jobs better.

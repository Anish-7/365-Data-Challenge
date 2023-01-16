# Challenge

# CASE : 
365 Data Science is an online learning platform specializing in data science courses. Students learn by watching video content, then evaluate their knowledge by taking quizzes, practice exams, course exams, and career track exams. The exams can be attempted more than once.

# TASK :
 Task is to analyze a database, which shows student engagement with the 365 platform, and identify key areas of improvement. Keeping in mind the metrics that 365’s CEO might find useful, build a single-page dashboard or machine learning model. Share your findings with the community, uncover valuable insights, and gain meaningful experience working on a real-life database.

# Question

    1. Which courses are the most watched by students? How are they rated?
    
    2. How would you define engagement (examples could be onboarding, minutes watched on the platform, exams/quizzes taken, etc.)?
    
    3. What key performance indicators (KPIs) are relevant to the problem?
    
    4. How many students register each month? What fraction of these students are also onboarded?
    
    5. Do students watch more content with time? Is this seasonally dependent? Does it depend on marketing campaigns, promo periods, etc.?
    
    6. How do the students engage with the platform based on user type (free or paid), subscription type (monthly, quarterly, or annual), and country?
    
    7.Which are the countries with the most students registered? Does this number scale proportionally with the number of minutes watched per country?

# Building the Model 

- Classification : Task is to develop a machine learning model to predict whether a Free Plan user would convert to a paid subscriber or not.
    
    - Feature : 
        - Minutes watched on the platform (Decimal)
        - Number of days in which a student was engaged with the platform (Integer)
        - Engaged with quizzes (Boolean)
        - Engaged with exams (Boolean)
        - Engaged with the Q&A hub (Boolean)

    - Target:

        Subscribed (Boolean)

- FASTAPI - run application
    - uvicorn main:app

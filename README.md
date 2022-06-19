# Daily learning journal

## May 2
This is the first day of the capstone kickoff meeting.

## May 3

Today we had a talk with someone from Seasalt.AI. She gave us much useful 
### Logging is the best practice

If your code is being deployed, it becomes much more difficult to troubleshoot. A log file is saved somewhere else so that 

### Remember to document on the code

We should always support the in-code documentation with summarized plain-English explanations. There are three types of documentation: customer-facing, developer-facing, and auto-docs.

### Containerized deployment

For academic projects, we just use command lines and that's all good to go. However, in actual deployment, 

#### Docker

It can package and run an application in an isolated environment called a container. The key for docker is that it will always perform exactly the same, no matter whose machine it is running on.

#### Kubernetes

It is a portable, extensible, open source platform for managing containerized workloads. It acts like a clustering service which can manage all the resources, and schedule them. In the deployment stage, it defines the structure of the containers.

The overview of the [image](https://github.com/Georgeanna-Li/Capstone_CFI/blob/df76ea0a0832a864252f24ed42c1f8c5d17b8995/Screen%20Shot%202022-05-03%20at%2009.52.36.png) below is that whatever requests come from the website, there will be an `ingress` that's asking for services. And the services will route to available pods.



### CI/CD

CI(Continuous Integration)
- commit your changes regularly to source control;
- share code with other developers so that everything is compatible
- linging, checking for merge conflicts, building in dev

CD(Continuous Delivery)
- get changes of all types—including new features, configuration changes, bug fixes and experiments—into production, or into the hands of users, safely and quickly in a sustainable way


### Imposter syndrome

Naturally there's going to be some gaps between what we already know to what we need to know. But always remember we are not expected to know everything for an entry level position. We should look for an employer that sees our potential and willing to nurture it. 

- Don't be afraid to ask questions, but do it tactfully
- Ask for opportunities to learn
- Don't be afraid to dive into something new

Remember that soemtimes the naive method is the best choice - we don't have to try overcomplicate things all the time!



## May 4th

Today we met with our capstone partner Pavel from CFI, we proposed several strategies after carrying out EDA. We agreed on taking the first step on script text analysis where we use the script of each course as input, and the overall ratings of the course as labels, to train a model that can predict the quality of the script.

Later we can expand the idea to other categories such as customer user engagement etc.

## May 5th 

Today I read this article on [objective functions of regression and classification](https://medium.com/@bhanuyerra/objective-functions-used-in-machine-learning-9653a75363b5).



## May 6th

Case scenario: there's a company called TRUECAR. It's an online car selling platform. Every time a customer comes, the website will choose five top dealers for the customer based on its recommendation system.

(1) assume that TRUECAR gets $300 per successful deal regardless of the deal price. How would you recommend the top three dealers each time?

A: I would build up a classification system based on the label of 0(unsuccessful deal) and 1(successful deal). Using features such as the distance between the customer and the dealer, the customer user profile, their historical user behavior, this binary classification model predicts how likely the deal is to be made. Then I can rank them based on the probabilities and pick the top three dealers.

(2) now we know that TRUECAR offers a subscription plan to the dealers: for example, if they pay $1000 per month, we guarantee them that there will be 100 matches for them. If we fail to reach that number, we will give them back the proportion of the money. That being said, if we only give them 90 matches, we will give a refund of $100 at the end of the month. How would you modify the model you built?

A: This time I would take into account of the money the platform earns each time. I would multiply the probability by the money earned to rank the dealers and make recommendations.


## May 9th

Today we met with Jungyeul to discuss what we need to do for the text script extraction. He shared with us some [useful information like this article](https://medium.com/analytics-vidhya/text-classification-with-bert-using-transformers-for-long-text-inputs-f54833994dfd). And we are going to explore LongTransformer on it.

## May 10th

Today I tried to use `pysrt` model to clean the text data.

## May 11th

Today we met with Pavel, talked about what we did in this week. My main job is to extract linguistics features from the script and make suggestions on what aspect to be improved.


## May 12th

Looked for more linguistics features online and plug them into our model to see which features play the most important role.


## May 13th

Today I attended the speaker series from Scott, a current linguistics engineer at Amazon. He introduced the workflow from the product team to the long-term debugging lifecycle of a linguistics engineer.


## May 16th

Today we had a meeting with Jungyeul, and also shared our doubts with him. We are not sure what he meaned by "label" and "feature". We don't want to go with the LongTransformer and take raw text as input. We are going to try regression model first and see how those features are having impact on our final result.

## May 17th

I completed the regression model and conducted feature importance analysis.

## May 18th

I learned more about pandas dataframe.

## May 19th

I did SHAP analysis on the features that I extracted from the script.

## May 20th

I talked to my team members for what I did on the linguistics features. And we discussed what we wanted to do next week.

## May 24th

We have a meeting among our group members and we decided to look at features that could potentially influence the 

## May 25th

I started the training course on Kubernetes. The development of container is a huge step forward for all software developments. 


## May 26th 

The product team will propose something that they believe humans will tell Alexa to do. They come up with some excaamples and desired output. Then the engineering team will take a closer look at what they could do to the NLU model. 

ML models: expensive, but generalizes well

Scott also mentions that they are always on call to fix bugs. There isn’t always an obvious solution – there could be a million ways that something could go wrong. So the core of the job is always to keep a learning attitude at work.

## May 27th

We made the presentation for next week. The whole group discussed what should be done in the next stage of the project.

## May 30th

I applied for more jobs, including data science positions and machine learning positions.

## May 31th

Today I learned about [mutually exclusive events and independent events](https://byjus.com/maths/difference-between-mutually-exclusive-and-independent-events/#:~:text=The%20difference%20between%20mutually%20exclusive,occurrence%20of%20the%20other%20event.). 

The biggest difference is that mutually exclusive events means that either A will happen or either B will happen. Mutually exclusive indicates P(X and Y) = 0.

However, independent events can still have overlap in between them. Independence means P(X and Y) = P(X)P(Y).


## June 10th

[How to calculate the percentage under the normal distribution?](https://www.math.stonybrook.edu/~retakh/ams102/normal#:~:text=Consider%20the%20normal%20distribution%20N,P(z%20%3C%200.53).)




## June 13th

Today in the group we were discussing how to make our final presentation. We are trying to tell a story through the whole slides. Zimo is going to do the introduction part, then it's me introducting the NPS score, and then Chao Ding is responsible for explaining the model and the model performance. The final part is me and Jiang talking about data visualization.

## June 14th

Today we had a meeting with Jungyuel and Ryan to discuss if there's anything that we can improve in our final presentation slides. He mentioned some slides are too technical for managers to understand. We should keep the slides as simple as possible.

## June 15th

Today we went to downtown CFI office to do the presentation. Pavel gave us a lot of useful advice:
Slides suggestions:

1. Most important: simply the outline. 
    1. - Methodology 
    2. - machine learning model
    3. - Takeaways  (how to use this like this, what we can do more about this, where you can expect from this project in 6 months time

In the slides today, we are going to talk about the mothodology, ..

2. END OF COURSE SURVEY
The first line should tell people what this slide is about
“The survey has 5 questions, and the most important one is ***, and also there’s one question “
Entries and columns don’t needed
List five bullets points of the survey

3. Put the COURSE TRANSCRIPT and the previous one in one slide
Just show two or three of the course
“Each course is broke into sections, and they have timestamps for each line”
If you feel like they don’t need to know this kind of detail, you can exclude it

4. LINGUISTIC FEATURES: important
They have known the data source, and how do we logically separate this ? Are the linguistics features belong to the model? Or is it universal for everything?
“From the data source, we created the linguistics features, ***”
Take the EXTRA part out, take the count of courses out, for `summary statistics`, make each one a bullet/dash, few words introducing what this is.

Each bullet point can be a separate slide:
Why this is important? (In this part we are preparing people for the final model, the features)
For the  `sentiment	 analysis` and the `readability score` we have to introduce them more. Have an example for each one, you don’t have to go through them during the presentation, but keep it there for them to see.
Just keep one readability score there, quickly elaborate what this is. You can even stop on the point and see if there’s any questions. 


How do we transition into this? 
Just need a little part of each features

You can have question- answer pattern in the slides

5. NPS score
Start with the second slide, “this is the standard way of calculating the NPS score”, and then show the converted part of 
One bullet point: the distribution part looks pretty good, interesting to find a benchmark of the industry level of the courses. “You can always know how you are doing in the industry.”

6. Models with section level data
“Advanced machine learning model to predict the  NPS score”
This page is too technical. 
“We are very confident about the model”
If you put R2, then you will have to explain what the r2 is.
The more you go into technical terms, the easier you will lose them.

7. MODls trained with 
“This is something that will impact the model most. ”
How is chapter_count the most important feature?
“The chapter count will impact the model the most”.
“In my mind, if I see a course with 10 chapters whereas a course with 3 chapters”
How to say about the program？？

8. Color coded the 
Blue + orange / red + green
Put two courses together, we can see two levels
Bullet point, and space between (format it better)
Don’t need to say “SHAP VALUE”

9. FEATURE OUTLIERS
2nd page: two circles, have two courses side by side
“We need more  ”
Coherence meaning (…)

10. Introduce the section count (what is video level)

FMVA courses recommended (core courses) - change one
ESG: in the last pages  environmental social governance 
New requirements in the company you have to keep green

Just keep the first one

REMEMBER to pause, allow the users to think 
Don’t be afraid of the pause and the silence

## June 16th

I reviewed some math concepts including cross product, dot product, mutually exclusive, and independent events.

## June 17th

I did a machine learning job screening test, one of the questions is: [Count of distinct graphs that can be formed with N vertices](https://www.geeksforgeeks.org/count-of-distinct-graphs-that-can-be-formed-with-n-vertices/).

Given an integer N which is the number of vertices. The task is to find the number of distinct graphs that can be formed. Since the answer can be very large, print the answer % 1000000007.

EXAMPLE:
Input: N = 3 
Output: 8
Input: N = 4 
Output: 64 

Approach: 
 

The maximum number of edges a graph with N vertices can contain is X = N * (N – 1) / 2.
The total number of graphs containing 0 edge and N vertices will be XC0
The total number of graphs containing 1 edge and N vertices will be XC1
And so on from a number of edges 1 to X with N vertices
Hence, the total number of graphs that can be formed with n vertices will be:
XC0 + XC1 + XC2 + … + XCX = 2X.

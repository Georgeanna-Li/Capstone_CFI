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

## May 21th






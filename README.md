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







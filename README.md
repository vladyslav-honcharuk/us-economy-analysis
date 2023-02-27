# US econom analysis

Project completed while studying at MIT

The US economy is the largest in the world and the most interesting to discover, there are a lot of different kinds of businesses and each of them contributes to the whole. Analyzing the business and applying the possible actions is a great way to increase the interest from investors and make bigger profit. But each of the businesses is different and requires a separate analysis, from the quality of this analysis depends the future state of the business. To perform the analysis the complete and clear data which is stored in some database is needed. All of this handles ETL, an important technic, which is the first thing that is needed to be done before analyzing the data. There is a lot of indicators which may be helpfull when making a good decision, such as trends, seasonalities, percentage change etc. In my analysis of some of the businesses I was able to define the sectors of economy that become more profitable since 1982, and the ones that may seize to exist soon, also I described seasonalities of some of the businesses, which are patterns at a certain period of the year. The grocery stores are the most profitable business from all of the analyzed, book stores - are the least profitable.

In the project I needed to perform 2 main things - ETL (Extract-Transform-Load) process on the dataset and analysis of the cleaned data. ETL is a powerful tool to clean the data from the redundant parts, impute the missing values, or add additional data, encrypt the data and finally upload the data into the database on the server to make it available for multiple to people to work with or store the data remotely.

Analysis of the data is used to make prediction of the future state of the subject. In this project the data from the sales of different kinds of businesses from the USA is used. To take more insights from the data there is things such as trends which defines whether the values of a time series increase, decrease or stay the same over certain period of time, percentage change which defines how the value has changed over certain period of time and rolling time windows, which allow to upply some functions on a subset of values from the whole set of data, such as a moving average n function which takes each n values from the time series and computes their mean, and then the new set of data is created after that.

The task is to perform the whole process of ETL - open the file and transform it in the one, that will satisfy the requiremens that the dataset need to follow to be able to perform an analysis with it, and upload the file into database in MySQL Server locally. Then with the help of MySQL write differnt queries in the Python IDE to extract the needed information to complete the final step - build grapths that will visualy represent the patterns, trends and seasonalities of the data of certain businesses. And finaly, make an explanation for each graph.

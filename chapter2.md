---
title       : Metacharacters I
description : In this chapter I will teach you about metacharacters
attachments :
  slides_link : https://s3.amazonaws.com/assets.datacamp.com/course/teach/slides_example.pdf

--- type:MultipleChoiceExercise lang:r xp:50 skills:1 key:ab57cc6e24
##Wildcard

The wildcard **.** represent any character in a regular expression. It means that **.** represents any character *that exists* in a given position. **Which of the following texts does not match with the regular expression */Hell./*   ?**

*** =instructions
- Hell
- Hell is warm
- Hello, how are you?
- I love Hellene
*** =hint
Remember the wildcard match any character that *exists*
*** =sct
```{r}
#
msg_bad_1 <- "In this instance the wildcard matches with a `space`"
msg_bad_2 <- "In this instance the wildcard matches with an `o`"
msg_bad_3 <- "In this instance the wildcard matches with an `e`"
msg_success <- "Exactly! In this intance, there is no character after Hell, therefore the regex doesn't match"


test_mc(correct = 1, feedback_msgs = c(msg_success, msg_bad_1, msg_bad_2, msg_bad_3 )) 
```

--- type:NormalExercise lang:r xp:50 skills:1 key:452b676422
##Text and string/character variables

In the previous exercise we learned that regular expression can be used in *string* or so called in R *character* variables. However; we need to see the structucture of this character to understand how to select the best strategy for using *regex*

*** =instructions
- Load the movies database 
- Create a vector called `title`
- Observe the first 15 observations of the title vector looks like using the function head
- After reflecting of the structure character vector click the "Submit Answer" button


*** =hint
- Please run the code shown in the item
- Please run the code shown in the item
- Please run the code shown in the item

*** =pre_exercise_code
```{r}
```
*** =sample_code
```{r}

# Uncomment the line below & click control+R
# movies <- read.csv("http://s3.amazonaws.com/assets.datacamp.com/course/introduction_to_r/movies.csv", stringsAsFactors=F)

# Store the title variable from the movie dataframe in titles vector, uncomment the line below
# Uncomment the line below & click control+R
#titles<-movies$title

# Observe the first 15 observations in the title variable from the movie dataframe, uncomment the line below
# Uncomment the line below & click control+R
#head(titles, 15)

# When you have reflected about the structure of the data click "Submit Answer"


```

*** =solution
```{r}
# Uncomment the line below & click control+R
movies <- read.csv("http://s3.amazonaws.com/assets.datacamp.com/course/introduction_to_r/movies.csv", stringsAsFactors=F)

# Store the title variable from the movie dataframe in titles vector, uncomment the line below
# Uncomment the line below & click control+R
titles<-movies$title

# Observe the first 15 observations in the title variable from the movie dataframe, uncomment the line below
# Uncomment the line below & click control+R
head(titles, 15)

# When you have reflected about the structure of the data click "Submit Answer"


```

*** =sct
```{r}
test_error()
test_object("movies")
test_object("titles")

test_function(name="head", args='x', not_called_msg = "Make sure to call the function [`head()`](http://www.rdocumentation.org/packages/utils/functions/head) show explore the values of `titles`.",
              incorrect_msg = "Have you passed the correct variable to the function [`head()`](hhttp://www.rdocumentation.org/packages/utils/functions/head)?")   

# It's always smart to include the following line of code at the end of your SCTs
# It will check whether executing the student's code resulted in an error, 
# and if so, will cause the exercise to fail


# Final message the student will see upon completing the exercise
success_msg("Good work!")
```
--- type:MultipleChoiceExercise lang:r xp:50 skills:1 key:0d507f6f0e
##Regular expressions jargon!

Regulars expressions have 2 main components. The *literals* and the *metacharacters*. The literals are any *number*, *alphabetic* or **some** *signs* that have no other meaning than themselves. *1* means *1*, *a* means *a*, *,* means *,*. The *spaces*, *tabulation*, *line breaks* all of them are *literals*. The metacharacters have a special meaning, and we discuss them later. They are always: *.  \  ^  $  ?  +  ( )  [ ]  { }*. This ones can change according to the context: *, -*
**Which of the following regex contains at least a metacharacter?**

*** =instructions
- Hello, my name is Peter Parker!
- What is your name?
- I don't have time for your foolishness: 
- Be my guest!
*** =hint
Have a look at heading of this exercise and observe that it refers to a specific file in this list?
*** =sct
```{r}
# The sct section defines the Submission Correctness Tests (SCTs) used to
# evaluate the student's response. All functions used here are defined in the 
# testwhat R package

msg_bad <- "There is no metacharacter in this regex"
msg_success <- "Exactly! the question mark ? is a metacharacter"

# Use test_mc() to grade multiple choice exercises. 
# Pass the correct option (Action, option 2 in the instructions) to correct.
# Pass the feedback messages, both positive and negative, to feedback_msgs in the appropriate order.
test_mc(correct = 2, feedback_msgs = c(msg_bad, msg_success, msg_bad,msg_bad)) 
```

--- type:NormalExercise lang:r xp:50 skills:1 key:452b6764ff
##Using literals

In a previous exercise we learned the *literal*. In R, the function `grep` must have at least 2 arguments, the first one is a *regular expression* or *regex* and the second one is a test character vector. It returns a numeric vector of the indices of the original vector, where the regex match the string

*** =instructions
- The environment is populated with a character vector `titles`
- Fill in the blank with the proper *regex*


*** =hint
- Remember the literal values represent themselves


*** =pre_exercise_code
```{r}
library(gtools)
movies <- read.csv("http://s3.amazonaws.com/assets.datacamp.com/course/introduction_to_r/movies.csv", stringsAsFactors=F)
titles<-movies$title
rm(movies)

```
*** =sample_code
```{r}

#The environment is populated with the vector `titles`

#Replace ____ below with the proper regular expression 
#in order to find out how many movies has the word "Time" in their title
#Don't change anything else!
regex <- "____"
length(grep(regex, titles,value=T))

```

*** =solution
```{r}
#The environment is populated with the vector `titles`

#Replace ____ below with the proper regular expression
#in order to find out how many movies are the word "Time" in their title
#Don't change anything else!
regex <- "Time"
length(grep(regex, titles,value=T))

```

*** =sct
```{r}
regex.sln<-function(r){
if (regex==r)  {
success_msg("Good work!")
}else{
err_msg <- paste('The regex `', regex, '` is incorrect', sep="")
test_an_object("regex", undefined_msg = err_msg)
}}
regex.sln("Time")

```
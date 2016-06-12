---
title       : Metacharacters I
description : In this chapter I will teach you about metacharacters
attachments :
  slides_link : https://s3.amazonaws.com/assets.datacamp.com/course/teach/slides_example.pdf

--- type:MultipleChoiceExercise lang:r xp:50 skills:1 key:ab57cc6e24
##Wildcard .

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
##The escape I from metacharacters to literals: \
As I mentioned before the metacharacters have *special meaning*, however what if I want to give a *literal sense*, for instance a dot actually means dot, a question mark that really means a question mark. In such case you need to *escape* the metacharacter with the escape metacharacter or *\*. **In R and Java, you need two bashlashes to escape a metacharacter!!**

*** =instructions
- I have loaded a movie titles vector from the movies database
- Use the proper regex to know how many titles do have a dot in their titles? 
- Use the proper regex to know how many titles do have a question mark in their titles? 
- Use the proper regex to know how many titles do have a backslash in their titles? 


*** =hint
- Please run the code shown in the item
- Please run the code shown in the item
- Please run the code shown in the item

*** =pre_exercise_code
```{r}
movies <- read.csv("http://s3.amazonaws.com/assets.datacamp.com/course/introduction_to_r/movies.csv", stringsAsFactors=F)
titles <- movies$title
rm(movies)
```
*** =sample_code
```{r}
#I have loaded a title vector of movie titles
# Complete the ___ with the correct regex in order to answer the questions
# Don't do any other change in the script!

#How many movies contains a dot (.) in their titles
regex.dot <- '____'
length(grep(regex.dot, titles))

#How many movies contains a question mark (?) in their titles
regex.quest <- '____'
length(grep(regex.quest, titles))

#How many movies contains a backslash (\) in their titles
regex.bl <- '____'
length(grep(regex.bl, titles))

```

*** =solution
```{r}
#I have loaded a title vector of movie titles
# Complete the ___ with the correct regex in order to answer the questions
# Don't do any other change in the script!

#How many movies contains a dot (.) in their titles
regex.dot <- '\\.'
length(grep(regex.dot, titles))

#How many movies contains a question mark (?) in their titles
regex.quest <- '\\?'
length(grep(regex.quest, titles))

#How many movies contains a backslash (\) in their titles
regex.bl <- '\\\\'
length(grep(regex.bl, titles))

```

*** =sct
```{r}
test_error()
test_object("regex.dot")
test_object("regex.quest")
test_object("regex.bl")

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
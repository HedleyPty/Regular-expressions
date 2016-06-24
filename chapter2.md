---
output: word_document
---
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
As I mentioned before the metacharacters have *special meaning*, however what if I want to give a *literal sense*, for instance a dot actually means dot, a question mark that really means a question mark. In such case you need to *escape* the metacharacter with the escape metacharacter or \\. **In R and Java, you need two bashlashes or \\\\ to escape a metacharacter!!**

*** =instructions
- I have loaded a movie titles vector from the movies database
- Use the proper regex to know how many titles do have a dot in their titles? 
- Use the proper regex to know how many titles do have a question mark in their titles? 
- Use the proper regex to know how many titles do have a backslash in their titles? 


*** =hint
- Remember 2 things: in R you need a double backslash to escape a metacharacter!!

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

--- type:NormalExercise lang:r xp:150 skills:1 key:452b67642c
##The escape II literals with special meaning: \

As I mentioned before the escape character \\ eliminate the *special meaning* of the metacharacter it modifies. However in the other hand, it gives a special meaning to some literal characters. **In R and Java, you need two bashlashes or \\\\ to escape a metacharacter!!**

*** =instructions
- I have loaded a movie titles vector from the movies database
- You might need to answer some questions
- Use the following list of literal characters modified by \\ to solve the questions in the excercise:
- \\d means "any number"
- \\D means "any character but a number"
- \\w means "any printable character"
- \\W means "any non-printable character"
- \\s means "any white space character"
- \\S means "any non-white space character"
- \\b means "word boundary"
- \\t means "tab"
- \\n means "next line"
- Use the proper regex to know how many titles do have a backslash in their titles? 


*** =hint
- Remember 2 things: in R you need a double backslash to escape a metacharacter!!

*** =pre_exercise_code
```{r}
movies <- read.csv("http://s3.amazonaws.com/assets.datacamp.com/course/introduction_to_r/movies.csv", stringsAsFactors=F)
titles <- movies$title
rm(movies)
```
*** =sample_code
```{r}
#I have loaded a title vector of movie titles
#It will be needed to answer some questions
# Complete the ___ with the correct character in order to answer the questions
# Never use w, D, s or S in any case!
# Don't do any other change in the script!

#Complete the following regex with the correct characters!
regex.1 <- 'Your score is \\__\\__\\__\\__'
grepl(regex.1, 'Your score is 67.8')

#Complete the following regex with the correct characters!
regex.2 <- "My name is Gill\\__\\__I am a very proficient computer scientist, don't you think so\\__"
grepl(regex.2, "My name is Gill.
I am a very proficient computer scientist, don't you think so?")

#How many movies contains a tab in their titles
regex.tab <- '____'
length(grep(regex.tab, titles))

#How many movies contains at least two consecutive numbers in their titles
regex.numbers <- '____'
length(grep(regex.numbers, titles))

```

*** =solution
```{r}
#I have loaded a title vector of movie titles
#It will be needed to answer some questions
# Complete the ___ with the correct character in order to answer the questions
# Never use w, D, s or S in any case!
# Don't do any other change in the script!

#Complete the following regex with the correct characters!
regex.1 <- 'Your score is \\d\\d\\.\\d'
grepl(regex.1, 'Your score is 67.8')

#Complete the following regex with the correct characters!
regex.2 <- "My name is Gill\\.\\nI am a very proficient computer scientist, don't you think so\\?"
grepl(regex.2, "My name is Gill.
I am a very proficient computer scientist, don't you think so?")

#How many movies contains a tab in their titles
regex.tab <- '\\t'
length(grep(regex.tab, titles))

#How many movies contains at least two consecutive numbers in their titles
regex.numbers <- '\\d\\d'
length(grep(regex.numbers, titles))

```

*** =sct
```{r}
test_error()
test_object("regex.1")
test_object("regex.2")
test_object("regex.tab")
test_object("regex.numbers")

success_msg("Good work!")
```

--- type:MultipleChoiceExercise lang:r xp:50 skills:1 key:ab57cd6e24
##Analyzing a Python file

You can read any kind of code or program using R. I have loaded a Python file in the working directory. Use the R function **list.files()** to show the python file in the working directory. Read the file using the R function **python <- readLines("python file.py")**. **Which of the following regular expressions (in R) does determine the attributes of a Python class?**
*** =pre_exercise_code
```{r}
python.file <- c( "import math",
                  "class gameObject:",
                  "    def __init__(self, pos, radius):",
                  "        self.pos=pos",
                  "        self.radius=radius",

                  "def distance(Coord_1,Coord_2):",
                  '    if len(Coord_1) != len(Coord_2)',
                  '        return "The length of the vectors is not equal"',
                  "    else:",
                  "        l=[(Coord_1[i]-Coord_2[i])**2 for i in range(len(Coord_1))]",
                  
                  "        return math.sqrt(sum(l))",
                  "def collisions(x,y):",
                  "    Coord_x = x.pos",
                  "    Coord_y = y.pos",
                  "    impact = x.radius + y.radius",
                  '    if distance(Coord_x, Coord_y) <= impact:',
                  '    return "boom"' ) 
write.table(python.file, "python file.py",quote=F, col.names=F, row.names=F, sep="\n")
rm(python.file)
```

*** =instructions
- class
- self.
- self\\\\.
- self\\.
*** =hint
Remember the wildcard match any character that *exists*
*** =sct
```{r}
#
msg_bad_1 <- "`class` makes no sense in this context"
msg_bad_2 <- "`.` is a wildcard, it matches with anything"
msg_bad_3 <- "`\\` in R is not the metacharacter for escape"
msg_success <- "Exactly! This is correct!"


test_mc(correct = 3, feedback_msgs = c(msg_bad_1, msg_bad_2, msg_success, msg_bad_3 )) 
```

--- type:MultipleChoiceExercise lang:r xp:50 skills:1 key:0d507f6f0e
##Parentheses ()

The pair of parenthesis has **no meaning** in isolation. They have a special meaning, but we discuss that in future exercises. 
**Which of the following regex does match the string "(a)"?**  Use the R sintaxis 
*** =pre_exercise_code
```{r}

```
*** =instructions
- (a
- ^\\\\(a\\\\)$
- ^(a)$ 
- a)

*** =hint
Remember what you have learned about the escape metacharacter?
*** = sct
```{r}
msg_bad_1 <- "This regex leads to a compiling error!"
msg_bad_2 <- "This regex does not match the string, we will discuss ^ and $ in future chapters"
msg_success <- "Exactly! This is correct!"


test_mc(correct = 2, feedback_msgs = c(msg_bad_1, msg_success, msg_bad_2,  msg_bad_1 )) 
```
--- type:NormalExercise lang:r xp:50 skills:1 key:452b6764ff
##The alternation (|)

In a previous exercise we learned the *a set of parenthesis in isolation are meaningless*. The **alternation** represent a list of posibilities separated |

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

#Complete ____ the regular expression below 
#in order to find out how many movies has either the word "Time" or the word "World" in their title
#Don't change anything else!
regex <- "(Time____"
length(grep(regex, titles,value=T))

```

*** =solution
```{r}

#The environment is populated with the vector `titles`

#Complete ____ the regular expression below 
#in order to find out how many movies has either the word "Time" or the word "World" in their title
#Don't change anything else!
regex <- "(Time|World)"
length(grep(regex, titles,value=T))

```

*** =sct
```{r}
test_error()
test_object("regex")
success_msg("Good work!")
```
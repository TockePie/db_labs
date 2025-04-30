---
title: Проєктування баз даних
outline: deep
---

# Проєктування баз даних

## Модель бізнес-об'єктів

**Модель бізнес-об'єктів** - це опис системи, в рамках якої відображаються всі об’єкти (сутності) даної системи. [[1]](https://economyandsociety.in.ua/journals/7_ukr/82.pdf)

<center style="
    border-radius:4px;
    border: 1px solid #cfd7e6;
    box-shadow: 0 1px 3px 0 rgba(89,105,129,.05), 0 1px 1px 0 rgba(0,0,0,.025);
    padding: 1em;">

@startuml

left to right direction

entity User #52f752
entity User.id #aaffaa
entity User.first_name #aaffaa
entity User.last_name #aaffaa
entity User.email #aaffaa
entity User.phone_number #aaffaa
entity User.password #aaffaa
entity User.age #aaffaa

User.id -d-* User
User.first_name -d-* User
User.last_name -d-* User
User.email -d-* User
User.phone_number -d-* User
User.password -d-* User
User.age -d-* User

entity Answer #f74564
entity Answer.id #FFC0CB
entity Answer.content #FFC0CB
entity Answer.user_id #FFC0CB
entity Answer.question_id #FFC0CB
entity Answer.answer_id #FFC0CB

Answer.id -d-* Answer
Answer.content -d-* Answer
Answer.user_id -d-* Answer
Answer.question_id -d-* Answer
Answer.answer_id -d-* Answer

entity Variant #9966CC
entity Variant.id #9932CC
entity Variant.text #9932CC

Variant.id --* Variant
Variant.text --l-* Variant

entity SelectedVar #C23B22
SelectedVar "0,* " <-u-> "1,1" Variant
SelectedVar "0,* " <-d-> "1,1" Answer

entity Question #d147d1
entity Question.id #D8BFD8
entity Question.description #D8BFD8
entity Question.quiz_id #D8BFD8
entity Question.header #D8BFD8

Question.id -d-* Question
Question.description -d-* Question
Question.quiz_id -d-* Question
Question.header -d-* Question

Question "1,1" <- "0,*" Answer 
Variant "0,*" -u-> "1,1" Question

entity Type #117d59
entity Type.id #1ee8a4
entity Type.description #1ee8a4
entity Type.question_id #1ee8a4

Type.id -d-* Type
Type.description -d-* Type
Type.question_id -d-* Type

entity Result #00ff61
entity Result.id #00ff61
entity Result.content #00ff61
entity Result.name #00ff61
entity Result.answer_id #00ff61

Result.id -d-* Result
Result.content -d-* Result
Result.name -d-* Result
Result.answer_id -d-* Result

entity Feedback #f59e51
entity Feedback.id #FFDAB9
entity Feedback.title #FFDAB9
entity Feedback.description #FFDAB9
entity Feedback.date #FFDAB9
entity Feedback.user_id #FFDAB9
entity Feedback.quiz_id #FFDAB9

Feedback.id -d-* Feedback
Feedback.title -d-* Feedback
Feedback.description -d-* Feedback
Feedback.date -d-* Feedback
Feedback.user_id -d-* Feedback
Feedback.quiz_id -d-* Feedback

entity Quiz #06bfbf
entity Quiz.id #9effff
entity Quiz.owner_id #9effff
entity Quiz.description #9effff
entity Quiz.is_active #9effff
entity Quiz.creation_date #9effff
entity Quiz.close_date #9effff
entity Quiz.title #9effff

Quiz.id -d-* Quiz
Quiz.owner_id -d-* Quiz
Quiz.description -d-* Quiz
Quiz.is_active -d-* Quiz
Quiz.creation_date -d-* Quiz
Quiz.close_date -d-* Quiz
Quiz.title -d-* Quiz

entity Role #0c56bd
entity Role.id #aaddff
entity Role.name #aaddff
entity Role.description #aaddff

Role.id -d-* Role
Role.name -d-* Role
Role.description -d-* Role

entity Permission #14f749
entity Permission.id #ccee88
entity Permission.name #ccee88
entity Permission.description #ccee88

Permission.id -d-* Permission
Permission.name -d-* Permission
Permission.description -d-* Permission

entity WorkflowEvent #FFA500
entity WorkflowEvent.id #FFD700
entity WorkflowEvent.datetime #FFD700
entity WorkflowEvent.state #FFD700
entity WorkflowEvent.description #FFD700

WorkflowEvent.id -d-* WorkflowEvent
WorkflowEvent.datetime -d-* WorkflowEvent
WorkflowEvent.state -d-* WorkflowEvent
WorkflowEvent.description -d-* WorkflowEvent

entity EventParticipant #9370DB
entity EventParticipant.id #D8BFD8
entity EventParticipant.role #D8BFD8

EventParticipant.id -d-* EventParticipant
EventParticipant.role -d-* EventParticipant

Quiz "1,1" <-- "0,*" Question

User "1, 1" <-- "0, *" Answer : user_id
User "1, 1" -- "0, *" Feedback : user_id
User "1, 1" -- "0, *" Quiz : owner_id
User "1, 1" --> "0, *" Role
User "1, 1" -- "0 .. *" Permission
Question "0, *" --> "1,1" Type 
Question "1, 1" -- "0 .. *" Answer : question_id
Answer "0 .. *" -- "1, 1" Result : answer_id

Quiz "1, 1" -- "0 .. *" Feedback  
Role "1, 1" -- "0 .. *" Permission : RolePermission

WorkflowEvent "0,*" --> "1,1" User: initiator
WorkflowEvent "1,1" --> "1,1" Quiz
EventParticipant "0,*" --> "1,1" WorkflowEvent
EventParticipant "0,*" --> "1,1" User

@enduml

</center>

## ER-модель   

**ER-модель** описує сутності системи та визначає зв'язки між ними. [[2]](https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model)

<center style="
    border-radius:4px;
    border: 1px solid #cfd7e6;
    box-shadow: 0 1px 3px 0 rgba(89,105,129,.05), 0 1px 1px 0 rgba(0,0,0,.025);
    padding: 1em;"
>

@startuml
left to right direction
skinparam linetype polyline
skinparam nodesep 80
skinparam ranksep 80

entity EventParticipant {
    * id : UUID
    --
    role : TEXT
}

entity WorkflowEvent {
    * id : UUID
    --
    datetime : DATETIME
    state : TEXT
    description : TEXT
}

entity User {
    * id : UUID
    --
    first_name : VARCHAR
    last_name : VARCHAR
    email : VARCHAR
    password : VARCHAR
    phone_number : VARCHAR
    age : SMALLINT
}

entity Role {
    * id : UUID
    --
    name : VARCHAR
    description : TEXT
}

entity Permission {
    * id : UUID
    --
    name : VARCHAR
    description : TEXT
}

entity Quiz {
    * id : UUID
    --
    title : VARCHAR
    description : TEXT
    creation_date : DATETIME
    close_date : DATETIME
    is_active : BOOLEAN
    owner_id : UUID
}

entity Feedback {
    * id : UUID
    --
    title : VARCHAR
    description : TEXT
    date : DATETIME
    user_id : UUID
    quiz_id : UUID
}

entity Question {
    * id : UUID
    --
    quiz_id : UUID
    header : VARCHAR
    description : TEXT
}

entity Type {
    * id : UUID
    --
    question_id : UUID
    description : TEXT
}

entity Variant {
    * id : UUID
    --
    text : TEXT
}

entity SelectedVar {
    * id : UUID
    --
}

entity Answer {
    * id : UUID
    --
    content : TEXT
    user_id : UUID
    question_id : UUID
    answer_id : UUID
}

entity Result {
    * id : UUID
    --
    content : TEXT
    name : VARCHAR
    answer_id : UUID
}

EventParticipant "0..*" --> "1.1" WorkflowEvent
EventParticipant "0..*" --> "1.1" User

WorkflowEvent "0..*" --> "1.1" User
WorkflowEvent "1.1" -- "1.1" Quiz

User "1.1" --> "0..*" Role
User "1.1" -- "0.*" Feedback

Permission "0..*" -- "1.1" User
Role "1.1" --> "0..*" Permission

Quiz "1.1" -- "0..*" Feedback
Quiz "0..*" --> "1.1" User

Question "0.*" --> "1.1" Quiz  
Question "0..*" --> "1.1" Type

Variant "0.*" --> "1.1" Question
Variant "1.1" <--> "0.*" SelectedVar

Answer "0.*" --> "1.1" User
Answer "0.*" --> "1.1" Question
Answer "0..1" <--> "0.*" SelectedVar

Result "1.1" -- "0.*" Answer

@enduml

</center>

## Реляційна схема

**Реляційна схема** - це набір таблиць, кожна з яких відповідає за одну з сутностей реляційної бази даних, та зв'язків між ними. Реляційна схема використовується для представлення реляційної бази даних. [[3]](https://www.sciencedirect.com/topics/computer-science/relational-schema#:~:text=A%20relational%20schema%20is%20a,applications%20belong%20to%20one%20schema.)

<center style="
    border-radius:4px;
    border: 1px solid #cfd7e6;
    box-shadow: 0 1px 3px 0 rgba(89,105,129,.05), 0 1px 1px 0 rgba(0,0,0,.025);
    padding: 1em;"
>

![Реляційна схема](..%2Fimg%2Frelational_schema1.jpg)
</center>

## Посилання

1. [Бізнес-моделі підприємства: еволюція та класифікація](https://economyandsociety.in.ua/journals/7_ukr/82.pdf)
2. [Entity–relationship model](https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model)
3. [Relational Schemas](https://www.sciencedirect.com/topics/computer-science/relational-schema#:~:text=A%20relational%20schema%20is%20a,applications%20belong%20to%20one%20schema.)

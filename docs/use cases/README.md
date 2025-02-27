# Модель прецедентів

## Загальна схема

<center style="
    border-radius:4px;
    border: 1px solid #cfd7e6;
    box-shadow: 0 1px 3px 0 rgba(89,105,129,.05), 0 1px 1px 0 rgba(0,0,0,.025);
    padding: 1em;"
>

@startuml

    actor Expert
    actor Client

    usecase "UserManageAccount\nВзаємодія з\nобліковим записом" as UInteraction
    usecase "SurveyInteraction\nВзаємодія з опитуванням" as EInteraction
    usecase "SurveyCreate\nСтворити\nопитування" as SCreate
    usecase "SurveyDelete\nВидалити\nопитування" as SDelete
    usecase "SurveyManageResults\nВзаємодія\nз результатами" as SResults
    usecase "SurveyShareAccess\nПоділитись\nопитуванням" as SShare
    usecase "SurveyUpdate\nОновлення опитування" as SUpdate

    Expert -d-|> Client
    Expert -> EInteraction
    Client -u-> SResults
    Client -r-> SCreate
    Client -d-> UInteraction
    Client -d-> SDelete
    Client -d-> SUpdate
    Client -l-> SShare

@enduml

</center>

## Схема клієнта

<center style="
    border-radius:4px;
    border: 1px solid #cfd7e6;
    box-shadow: 0 1px 3px 0 rgba(89,105,129,.05), 0 1px 1px 0 rgba(0,0,0,.025);
    padding: 1em;"
>

@startuml

    left to right direction

    actor Client

    ' Група взаємодії з обліковим записом
    usecase "UserManageAccount\nВзаємодія з\nобліковим записом" as UInteraction
    usecase "UserRegistration\nРеєстрація" as URegister
    usecase "UserLogin\nВхід у систему" as ULogin

    UInteraction -u-> URegister
    UInteraction -u-> ULogin

    ' Група взаємодії з результатами
    usecase "SurveyManageResults\nВзаємодія\nз результатами" as SResults
    usecase "SurveyResultsView\nПерегляд відповідей" as SView
    usecase "UserCompletesSurvey\nЗаповнення опитування" as SComplete

    SResults -d-> SView
    SResults -d-> SComplete

    ' Інші сценарії роботи з опитуваннями
    usecase "SurveyCreate\nСтворення опитування" as SCreate
    usecase "SurveyUpdate\nОновлення опитування" as SUpdate
    usecase "SurveyDelete\nВидалення опитування" as SDelete
    usecase "SurveyReminder\nНагадування" as SReminder

    usecase "UserEditResponses\nРедагування відповідей" as SEdit
    usecase "SurveyResultsExport\nЕкспорт результатів" as SExport
    usecase "SurveyFeedback\nНадання відгуку" as SFeedback

    Client -[hidden]-> UInteraction

    ' Зв'язки клієнта
    Client -u-> UInteraction
    Client -d-> SResults
    Client -l-> SCreate
    Client -d-> SReminder
    Client -l-> SFeedback

    ' Допоміжні сценарії
    SView ..> SExport
    SComplete ..> SEdit
    SCreate ..> SUpdate
    SCreate ..> SDelete

@enduml

</center>

## Example

В цьому файлі необхідно перелічити всі документи, розроблені в проекті та дати посилання на них.

_Модель прецедентів повинна містити загальні оглядові діаграми та специфікації прецедентів._

Вбудовування зображень діаграм здійснюється з використанням сервісу [plantuml.com](https://plantuml.com/).

В markdown-файлі використовується опис діаграми

```html
<center style="
    border-radius:4px;
    border: 1px solid #cfd7e6;
    box-shadow: 0 1px 3px 0 rgba(89,105,129,.05), 0 1px 1px 0 rgba(0,0,0,.025);
    padding: 1em;"
>

@startuml

    right header
        <font size=24 color=black>Package: <b>UCD_3.0
    end header

    title
        <font size=18 color=black>UC_8. Редагувати конфігурацію порталу
        <font size=16 color=black>Діаграма прецедентів
    end title


    actor "Користувач" as User #eeeeaa

    package UCD_1{
        usecase "<b>UC_1</b>\nПереглянути список \nзвітів" as UC_1 #aaeeaa
    }

    usecase "<b>UC_1.1</b>\nЗастосувати фільтр" as UC_1.1
    usecase "<b>UC_1.2</b>\nПереглянути метадані \nзвіту" as UC_1.2
    usecase "<b>UC_1.2.1</b>\nДати оцінку звіту" as UC_1.2.1
    usecase "<b>UC_1.2.2</b>\nПереглянути інформацію \nпро авторів звіту" as UC_1.2.2

    package UCD_1 {
        usecase "<b>UC_4</b>\nВикликати звіт" as UC_4 #aaeeaa
    }

    usecase "<b>UC_1.1.1</b>\n Використати \nпошукові теги" as UC_1.1.1
    usecase "<b>UC_1.1.2</b>\n Використати \nрядок пошуку" as UC_1.1.2
    usecase "<b>UC_1.1.3</b>\n Використати \nавторів" as UC_1.1.3



    User -> UC_1
    UC_1.1 .u.> UC_1 :extends
    UC_1.2 .u.> UC_1 :extends
    UC_4 .d.> UC_1.2 :extends
    UC_1.2 .> UC_1.2 :extends
    UC_1.2.1 .u.> UC_1.2 :extends
    UC_1.2.2 .u.> UC_1.2 :extends
    UC_1 ..> UC_1.2.2 :extends


    UC_1.1.1 -u-|> UC_1.1
    UC_1.1.2 -u-|> UC_1.1
    UC_1.1.3 -u-|> UC_1.1

    right footer
        Аналітичний портал. Модель прецедентів.
        НТУУ КПІ ім.І.Сікорського
        Киів-2020
    end footer

@enduml

**Діаграма прецедентів**

</center>
```

яка буде відображена наступним чином

<center style="
    border-radius:4px;
    border: 1px solid #cfd7e6;
    box-shadow: 0 1px 3px 0 rgba(89,105,129,.05), 0 1px 1px 0 rgba(0,0,0,.025);
    padding: 1em;"
>

@startuml

    right header
        <font size=24 color=black>Package: <b>UCD_3.0
    end header

    title
        <font size=18 color=black>UC_8. Редагувати конфігурацію порталу
        <font size=16 color=black>Діаграма прецедентів
    end title


    actor "Користувач" as User #eeeeaa

    package UCD_1{
        usecase "<b>UC_1</b>\nПереглянути список \nзвітів" as UC_1 #aaeeaa
    }

    usecase "<b>UC_1.1</b>\nЗастосувати фільтр" as UC_1.1
    usecase "<b>UC_1.2</b>\nПереглянути метадані \nзвіту" as UC_1.2
    usecase "<b>UC_1.2.1</b>\nДати оцінку звіту" as UC_1.2.1
    usecase "<b>UC_1.2.2</b>\nПереглянути інформацію \nпро авторів звіту" as UC_1.2.2

    package UCD_1 {
        usecase "<b>UC_4</b>\nВикликати звіт" as UC_4 #aaeeaa
    }

    usecase "<b>UC_1.1.1</b>\n Використати \nпошукові теги" as UC_1.1.1
    usecase "<b>UC_1.1.2</b>\n Використати \nрядок пошуку" as UC_1.1.2
    usecase "<b>UC_1.1.3</b>\n Використати \nавторів" as UC_1.1.3



    User -> UC_1
    UC_1.1 .u.> UC_1 :extends
    UC_1.2 .u.> UC_1 :extends
    UC_4 .d.> UC_1.2 :extends
    UC_1.2 .> UC_1.2 :extends
    UC_1.2.1 .u.> UC_1.2 :extends
    UC_1.2.2 .u.> UC_1.2 :extends
    UC_1 ..> UC_1.2.2 :extends


    UC_1.1.1 -u-|> UC_1.1
    UC_1.1.2 -u-|> UC_1.1
    UC_1.1.3 -u-|> UC_1.1

    right footer
        Аналітичний портал. Модель прецедентів.
        НТУУ КПІ ім.І.Сікорського
        Киів-2020
    end footer

@enduml

**Діаграма прецедентів**

</center>

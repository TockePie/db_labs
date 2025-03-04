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
    actor Client
    usecase "UserManageAccount\nВзаємодія з\nобліковим записом" as UInteraction
    usecase "UserRegistration\nРеєстрація" as URegister
    usecase "UserLogin\nВхід у систему" as ULogin
    usecase "SurveyManageResults\nВзаємодія\nз результатами" as SResults
    usecase "SurveyResultsView\nПерегляд відповідей" as SView
    usecase "SurveyResultsExport\nЕкспорт результатів" as SExport
    usecase "SurveyCreate\nСтворення опитування" as SCreate
    usecase "SurveyUpdate\nОновлення опитування" as SUpdate
    usecase "SurveyDelete\nВидалення опитування" as SDelete
    usecase "SurveyReminder\nНагадування" as SReminder
    usecase "SurveyShareAccess\nПоділитись опитуванням" as SShare
    SResults ..> SView
    SResults ..> SExport
    UInteraction ..> URegister
    UInteraction ..> ULogin
    Client -[hidden]-> UInteraction
    Client -[hidden]-> SResults
    Client -u-> UInteraction
    Client -d-> SResults
    Client -l-> SCreate
    Client -u-> SUpdate
    Client -u-> SDelete
    Client -d-> SReminder
    Client -r-> SShare
@enduml

</center>

## Сценарії використання

### SurveyResultsExport

| ID                     |                                                                                               SurveyResultsExport                                                                                               |
| :--------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| **Назва:**             |                                                                                         Експорт результатів опитування                                                                                          |
| **Учасники:**          |                                                                                               Користувач, система                                                                                               |
| **Передумови:**        |                                                                                              Опитування завершене                                                                                               |
| **Результат:**         |                                                                                Користувач отримує результати у вибраному форматі                                                                                |
| **Виключні ситуації:** |                                                                            Некоректний формат експорту - UnsupportedFormatException                                                                             |
| **Основний сценарій:** | 1. Користувач обирає опитування <br> 2. Вибирає формат експорту та надсилає запит (може виникнути UnsupportedFormatException) <br> 3. Система генерує файл <br> 4. Користувач отримує файл у потрібному форматі |

<center style="
    border-radius:4px;
    border: 1px solid #cfd7e6;
    box-shadow: 0 1px 3px 0 rgba(89,105,129,.05), 0 1px 1px 0 rgba(0,0,0,.025);
    padding: 1em;"
>

@startuml

    skinparam ActivityBackgroundColor #d1a6e2

    |Користувач|
    start;
    :обирає опитування;
    :вибирає формат експорту та надсилає запит;
    note right #D10000
    <b>Possible error:
    - UnsupportedFormatException
    end note


    |Система|
    :система генерує файл;

    |Користувач|
    :користувач отримує файл у потрібному форматі;


    stop;

@enduml

</center>

### SurveyUpdate

| ID                     |                                                                                                        SurveyUpdate                                                                                                         |
| :--------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| **Назва:**             |                                                                                                    Оновлення опитування                                                                                                     |
| **Учасники:**          |                                                                                                     Користувач, система                                                                                                     |
| **Передумови:**        |                                                                                          Опитування створене, але ще не завершене                                                                                           |
| **Результат:**         |                                                                                         Система зберігає оновлену версію опитування                                                                                         |
| **Виключні ситуації:** |                                                                                   Опитування вже активне або завершене — зміни неможливі                                                                                    |
| **Основний сценарій:** | 1. Користувач відкриває потрібне опитування для редагування <br> 2. Вносить зміни у формулювання запитань або налаштування <br> 3. Підтверджує оновлення <br> 4. Система зберігає зміни й оновлює поточну версію опитування |

<center style="
    border-radius:4px;
    border: 1px solid #cfd7e6;
    box-shadow: 0 1px 3px 0 rgba(89,105,129,.05), 0 1px 1px 0 rgba(0,0,0,.025);
    padding: 1em;"
>

@startuml

skinparam ActivityBackgroundColor #d1a6e2

    |Користувач|
    start;
    :користувач відкриває потрібне опитування для редагування;
    :вносить свої зміни та підтверджує нові зміни;
    note right #D10000
    <b>Possible error:
    - Опитування вже активне або завершене — зміни неможливі
    end note

    |Система|
    :система зберігає зміни й оновлює поточну версію опитування;


    stop;

@enduml

</center>

### SurveyShareAccess

| ID                     |                                                                        SurveyShareAccess                                                                         |
| :--------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| **Назва:**             |                                                                  Надання доступу до опитування                                                                   |
| **Учасники:**          |                                                                       Користувач, система                                                                        |
| **Передумови:**        |                                                                 Користувач є автором опитування                                                                  |
| **Результат:**         |                                                                Інші користувачі отримують доступ                                                                 |
| **Виключні ситуації:** |                                                                              Немає                                                                               |
| **Основний сценарій:** | 1. Користувач обирає опитування для спільного доступу <br> 2. Система генерує унікальне посилання <br> 3. Посилання надається користувачам, які отримують доступ |

<center style="
    border-radius:4px;
    border: 1px solid #cfd7e6;
    box-shadow: 0 1px 3px 0 rgba(89,105,129,.05), 0 1px 1px 0 rgba(0,0,0,.025);
    padding: 1em;"
>

@startuml

    skinparam ActivityBackgroundColor #d1a6e2

    |Користувач|
    start;
    :змінює формат опитування на формат спільного доступу;
    :копіює посилання;
    |Система|
    :генерує унікальне посилання;
    :надає посилання користувачу;
    |Користувач|
    :отримує доступ до опитування;
    :ділиться посиланням з іншими користувачами;

    |Інші Користувачі|
    :отримують доступ до опитування через посилання;

    stop;

@enduml

</center>

### SurveyFeedback

| ID                     |                                                                                                SurveyFeedback                                                                                                |
| :--------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| **Назва:**             |                                                                                        Надання відгуку про опитування                                                                                        |
| **Учасники:**          |                                                                                             Користувач, система                                                                                              |
| **Передумови:**        |                                                                   Користувач завершив проходження опитування та має авторизований доступ.                                                                    |
| **Результат:**         |                                                                        Відгук успішно збережений у системі та доступний адміністрації                                                                        |
| **Виключні ситуації:** |                                                                    Відгук не відправлено через технічну помилку або недоступність сервера                                                                    |
| **Основний сценарій:** | 1. Користувач переглядає підсумки опитування <br> 2. Оцінює якість запитань і надає зворотний зв’язок <br> 3. Система зберігає відгук <br> 4. Адміністратор може переглянути отримані відгуки в адмін-панелі |

<center style="
    border-radius:4px;
    border: 1px solid #cfd7e6;
    box-shadow: 0 1px 3px 0 rgba(89,105,129,.05), 0 1px 1px 0 rgba(0,0,0,.025);
    padding: 1em;"
>

@startuml

    skinparam ActivityBackgroundColor #d1a6e2

    |Користувач|
    start;
    :переглядає підсумки опитування;
    :оцінює якість запитань і надає зворотний зв’язок;

    |Система|
    :система зберігає відгук;
    note right #D10000
    <b>Possible error:
    - Відгук не відправлено через технічну помилку або недоступність сервера
    end note

    :надає посилання користувачу;

    |Адміністратор|
    :адміністратор може переглянути отримані відгуки в адмін-панелі;

    stop;

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

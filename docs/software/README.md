# Реалізація інформаційного та програмного забезпечення

В рамках проекту розробляється:

- SQL-скрипт для створення на початкового наповнення бази даних
- RESTfull сервіс для управління даними

## **SQL скрипти для ініціалізації та наповнення бази даних**

```sql
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE IF NOT EXISTS "User" (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS "Role" (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(100) NOT NULL,
    description TEXT
);

CREATE TABLE IF NOT EXISTS "Permission" (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(100) NOT NULL,
    description TEXT
);

CREATE TABLE IF NOT EXISTS user_roles (
    user_id UUID REFERENCES "User"(id) ON DELETE CASCADE,
    role_id UUID REFERENCES "Role"(id) ON DELETE CASCADE,
    PRIMARY KEY (user_id, role_id)
);

CREATE TABLE IF NOT EXISTS role_permissions (
    role_id UUID REFERENCES "Role"(id) ON DELETE CASCADE,
    permission_id UUID REFERENCES "Permission"(id) ON DELETE CASCADE,
    PRIMARY KEY (role_id, permission_id)
);

CREATE TABLE IF NOT EXISTS "WorkflowEvent" (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    description TEXT,
    user_id UUID REFERENCES "User"(id) ON DELETE CASCADE,
    quiz_id UUID REFERENCES "Quiz"(id) ON DELETE CASCADE
);

INSERT INTO "Role" (name, description) VALUES
('Admin', 'Full access to the system'),
('Editor', 'Can edit quizzes'),
('Viewer', 'Read-only access');

INSERT INTO "Permission" (name, description) VALUES
('Manage Users', 'Permission to manage users'),
('Edit Quizzes', 'Permission to edit quizzes'),
('View Content', 'Permission to view content');

INSERT INTO "User" (first_name, last_name, email, password) VALUES
('Olena', 'Kovalenko', 'olena@example.com', 'hashpass1'),
('Ivan', 'Petrenko', 'ivan@example.com', 'hashpass2'),
('Marta', 'Sydorenko', 'marta@example.com', 'hashpass3');

INSERT INTO user_roles (user_id, role_id) VALUES
((SELECT id FROM "User" WHERE email = 'olena@example.com'), (SELECT id FROM "Role" WHERE name = 'Admin')),
((SELECT id FROM "User" WHERE email = 'ivan@example.com'), (SELECT id FROM "Role" WHERE name = 'Editor')),
((SELECT id FROM "User" WHERE email = 'marta@example.com'), (SELECT id FROM "Role" WHERE name = 'Viewer'));

INSERT INTO role_permissions (role_id, permission_id) VALUES
((SELECT id FROM "Role" WHERE name = 'Admin'), (SELECT id FROM "Permission" WHERE name = 'Manage Users')),
((SELECT id FROM "Role" WHERE name = 'Editor'), (SELECT id FROM "Permission" WHERE name = 'Edit Quizzes')),
((SELECT id FROM "Role" WHERE name = 'Viewer'), (SELECT id FROM "Permission" WHERE name = 'View Content'));

INSERT INTO "WorkflowEvent" (created_at, description, user_id, quiz_id)
VALUES
    (
        NOW(),
        'Quiz initialized by the user',
        (SELECT id FROM "User" WHERE email = 'olena@example.com'),
        (SELECT id FROM "Quiz" WHERE title = 'Java Basics')
    ),
    (
        NOW(),
        'User is answering the questions',
        (SELECT id FROM "User" WHERE email = 'ivan@example.com'),
        (SELECT id FROM "Quiz" WHERE title = 'SQL Starter')
    ),
    (
        NOW(),
        'Quiz completed and submitted',
        (SELECT id FROM "User" WHERE email = 'marta@example.com'),
        (SELECT id FROM "Quiz" WHERE title = 'Java Basics')
    );

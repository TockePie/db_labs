# **Реалізація інформаційного та програмного забезпечення**

## SQL скрипти для ініціалізації та наповнення бази даних

```sql
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE IF NOT EXISTS "User" (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    phone_number VARCHAR(20),
    age SMALLINT
);

CREATE TABLE IF NOT EXISTS "Role" (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(255) NOT NULL,
    description TEXT
);

CREATE TABLE IF NOT EXISTS "Permission" (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(255) NOT NULL,
    description TEXT
);

CREATE TABLE IF NOT EXISTS user_roles (
    user_id UUID NOT NULL,
    role_id UUID NOT NULL,
    PRIMARY KEY (user_id, role_id),
    FOREIGN KEY (user_id) REFERENCES "User"(id) ON DELETE CASCADE,
    FOREIGN KEY (role_id) REFERENCES "Role"(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS role_permissions (
    role_id UUID NOT NULL,
    permission_id UUID NOT NULL,
    PRIMARY KEY (role_id, permission_id),
    FOREIGN KEY (role_id) REFERENCES "Role"(id) ON DELETE CASCADE,
    FOREIGN KEY (permission_id) REFERENCES "Permission"(id) ON DELETE CASCADE
);

CREATE TABLE Quiz (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    title VARCHAR(255) NOT NULL,
    description TEXT,
    creation_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    close_date TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE,
    owner_id UUID NOT NULL,
    FOREIGN KEY (owner_id) REFERENCES User(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Question (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    quiz_id UUID NOT NULL,
    header VARCHAR(255),
    description TEXT,
    FOREIGN KEY (quiz_id) REFERENCES Quiz(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Type (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    question_id UUID NOT NULL,
    description TEXT,
    FOREIGN KEY (question_id) REFERENCES Question(id) ON DELETE CASCADE
);

CREATE TABLE EventParticipant (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    role TEXT NOT NULL,
    user_id UUID NOT NULL REFERENCES "User"(id),
    event_id UUID NOT NULL REFERENCES WorkflowEvent(id)
);

CREATE TABLE Variant (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    question_id UUID NOT NULL,
    text TEXT NOT NULL,
    FOREIGN KEY (question_id) REFERENCES Question(id) ON DELETE CASCADE
);

CREATE TABLE SelectedVar (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    variant_id UUID NOT NULL,
    answer_id UUID NOT NULL,
    FOREIGN KEY (variant_id) REFERENCES Variant(id) ON DELETE CASCADE,
    FOREIGN KEY (answer_id) REFERENCES Answer(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS "Feedback" (
  id PRIMARY KEY,
  description TEXT NOT NULL,
  date TIMESTAMP NOT NULL,
  user_id  NOT NULL,
  survey_id ,

  CONSTRAINT fk_feedback_user FOREIGN KEY (user_id)
    REFERENCES User(id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,

  CONSTRAINT fk_feedback_survey FOREIGN KEY (survey_id)
    REFERENCES Survey(id)
    ON DELETE SET NULL
    ON UPDATE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_feedback_user ON "Feedback" (user_id);
CREATE INDEX IF NOT EXISTS idx_feedback_survey ON "Feedback" (survey_id);

INSERT INTO "Role" (name, description)
VALUES 
    ('Admin', 'Administrator role with full access'),
    ('Editor', 'Editor role with content editing permissions'),
    ('Viewer', 'Viewer role with read-only access');

INSERT INTO "Permission" (name, description)
VALUES 
    ('Manage Users', 'Permission to manage users'),
    ('Edit Content', 'Permission to edit content'),
    ('View Content', 'Permission to view content');

INSERT INTO "User" (first_name, last_name, email, password, phone_number, age)
VALUES
    ('Alice', 'Smith', 'alice@example.com', 'hashedpassword1', '+123456789', 30),
    ('Bob', 'Johnson', 'bob@example.com', 'hashedpassword2', '+987654321', 25),
    ('Charlie', 'Brown', 'charlie@example.com', 'hashedpassword3', '+192837465', 35);

INSERT INTO user_roles (user_id, role_id)
VALUES 
    ((SELECT id FROM "User" WHERE email = 'alice@example.com'), (SELECT id FROM "Role" WHERE name = 'Admin')),
    ((SELECT id FROM "User" WHERE email = 'bob@example.com'), (SELECT id FROM "Role" WHERE name = 'Editor')),
    ((SELECT id FROM "User" WHERE email = 'charlie@example.com'), (SELECT id FROM "Role" WHERE name = 'Viewer'));

INSERT INTO role_permissions (role_id, permission_id)
VALUES
    ((SELECT id FROM "Role" WHERE name = 'Admin'), (SELECT id FROM "Permission" WHERE name = 'Manage Users')),
    ((SELECT id FROM "Role" WHERE name = 'Editor'), (SELECT id FROM "Permission" WHERE name = 'Edit Content')),
    ((SELECT id FROM "Role" WHERE name = 'Viewer'), (SELECT id FROM "Permission" WHERE name = 'View Content'));

INSERT INTO Quiz (title, description, creation_date, close_date, is_active, owner_id)
VALUES
    ('Customer Satisfaction Quiz', 'Quiz about customer satisfaction', '2025-04-20 10:00:00', '2025-04-30 23:59:59', TRUE, 'e7b3f5b4-8a63-4e2e-baad-5a8c5c5b1234'),
    ('Employee Feedback Quiz', 'Quiz to collect employee feedback', '2025-04-21 12:00:00', NULL, TRUE, '0e00b3e1-2c66-4f56-9332-9e20bfcdb812'),
    ('Website Usability Quiz', 'Quiz to evaluate website usability', '2025-04-22 14:00:00', '2025-05-01 20:00:00', FALSE, '7f6c9aee-681c-4f61-812d-dcd7edb7b029');

INSERT INTO Question (quiz_id, header, description)
VALUES
    ('827487ea-227a-4847-9bf7-e0ada468c87e', 'How satisfied are you?', 'Please rate your satisfaction from 1 to 5'),
    ('827487ea-227a-4847-9bf7-e0ada468c87e', 'Would you recommend us?', ''),
    ('827487ea-227a-4847-9bf7-e0ada468c87e', 'What could we improve?', 'Open-ended feedback welcome'),
    ('827487ea-227a-4847-9bf7-e0ada468c87e', 'How easy was it to use our product?', 'Rate from 1 (hard) to 5 (easy)'),
    ('827487ea-227a-4847-9bf7-e0ada468c87e', 'Did everything work as expected?', '');

INSERT INTO Type (question_id, description)
VALUES
  ('f1b5084c-3e9a-485d-92e4-9b4696c2f953', '1TO5RATING'),
  ('11a6f19f-612c-4562-acba-a4573decb6ef', 'YES/NO'),
  ('68d46927-04b7-4d88-bf3d-6cd2d61e0756', 'TEXT'),
  ('654d25da-b39f-4bf0-9731-4872b7c3b5b3', '1TO5RATING'),
  ('b7135385-ca55-458c-b3f7-8c56c6449117', 'YES/NO');

INSERT INTO EventParticipant (role, user_id, event_id)
VALUES
  ('Reviewer', '359d3c13-30b6-4614-a54f-6d30bb5bd4ac', '20a8461b-03a6-4d4a-bd53-f33da214dbfc'),
  ('Submitter', '959d7ddf-12bb-4a3c-ae25-df4dbf60867e', 'c69418e5-38ae-4bc5-b6e8-ea98fc249aaf'),
  ('Observer', '959d7ddf-12bb-4a3c-ae25-df4dbf60867e', 'b5571635-803c-4fe0-95b1-382461510871');

INSERT INTO Feedback (content, date, user_id, survey_id)
VALUES ('This is some feedback content.', NOW(), 'dcd73fec-10fb-4bc5-8c01-938fa329af46', NULL);

INSERT INTO Variant (question_id, text)
VALUES
    ('f1b5084c-3e9a-485d-92e4-9b4696c2f953', 'Option 1'),
    ('f1b5084c-3e9a-485d-92e4-9b4696c2f953', 'Option 2'),
    ('11a6f19f-612c-4562-acba-a4573decb6ef', 'Yes'),
    ('11a6f19f-612c-4562-acba-a4573decb6ef', 'No');

INSERT INTO SelectedVar (variant_id, answer_id)
VALUES
    ('550e8400-e29b-41d4-a716-446655440000', '123e4567-e89b-12d3-a456-426614174000'), 
    ('6ba7b810-9dad-11d1-80b4-00c04fd430c8', '123e4567-e89b-12d3-a456-426614174001');
```

<!-- В рамках проекту розробляється:

- SQL-скрипт для створення на початкового наповнення бази даних


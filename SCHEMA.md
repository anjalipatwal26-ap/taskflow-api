# Database Schema

## User
| Field | Type | Constraints |
|---|---|---|
| id | UUID (String) | Primary Key |
| name | String(100) | Required |
| email | String | Required, Unique |
| password_hash | String | Required |
| created_at | Timestamp | Auto |
| updated_at | Timestamp | Auto |

## Task
| Field | Type | Constraints |
|---|---|---|
| id | UUID (String) | Primary Key |
| title | String(255) | Required |
| description | Text | Optional |
| status | String | Pending / In Progress / Completed |
| priority | String | Low / Medium / High |
| due_date | Timestamp | Optional |
| user_id | UUID (String) | Foreign Key -> User.id |
| created_at | Timestamp | Auto |
| updated_at | Timestamp | Auto |

## Relationship
One User has many Tasks (1:N). Deleting a User cascades to delete their Tasks.
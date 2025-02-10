1. User Setup

User, Role, Group, Biz Entity are 4 main concepts to manage the user of xAIBooks.

User is the human being using the system.

Biz Entity is who the system serves. 

Role is which function the user can use.

Group is which business entity the user can access.

1.1 Relationship

Each client of the Account Firm will be assigned a biz entity id and a group id. 

user - role: n-n

user - group: n-n

biz entity - group: n-n


1.2 General Setup

Role: Supervisor (all modules), Manager, Regular User


1.3 Supervisor:

Assign biz entity to group.

Assign group to user.

Assign modules to role.

1.4 User:

When login, 

1.4.1 if belonged to multiple groups, chose which group to continue.

If multiple biz entities in the selected group, chose which biz entity to continue. 

After chosing biz_entity, cannot manage other biz entities business.

1.4.2 if has multiple roles, chose which role to continue.


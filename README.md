# Cinema Hall

- Warning: Use `pytest app` for testing - not simple `pytest`
- Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before start

In `db/models.py` create table `CinameHall`. This table should have
such field:
- Char field `name`, name of the hall with maximum length of 50 
characters.
- Integer field `capacity`, the maximum number of spectators, that
the hall can accommodate.

Inside `app/main.py` make these actions:
1. Create:
   - Hall "Grey", with capacity equals to 180
   - Hall "Blue", with capacity equals to 70
   - Hall "Red", with capacity equals to 124
   - Hall "Orange", with capacity equals to 58
2. Update:
   - Hall "Grey", set capacity to 224
3. Delete:
   - Hall "Red"
4. Return:
   - Halls with capacity greater or equals to 70 and ordered by capacity


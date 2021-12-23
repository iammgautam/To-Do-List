[![Python version](https://img.shields.io/badge/Python-3.8-green?style=flat&logo=python)](https://docs.python.org/3.8/)
[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/zengboi/CLI-Login-System/blob/main/LICENSE)



# To DO List

A Simple CRUD (Create, Read, Update, Delete) Based To-Do List with User Authentication implemented fully using Class-Based Views

![Screenshot](https://github.com/zengboi/To-Do-List/blob/main/preview/task-list.png?raw=true)


## Run Locally

1. Clone the project

```bash
  git clone https://github.com/zengboi/To-Do-List.git
```

2. Go to the project directory

```bash
  cd To-Do-List
```

3. Install dependencies

```bash
  python3 -m venv your_virtualenv_name
  source ./your_virtualenv_name/bin/activate
  pip install -r requirements.txt

```

4. Start the Database Mirgation

```bash
  python manage.py makemigrations
  python manage.py migrate
```

5. Create a Admin User

```bash
    python manage.py createsuperuser
```

6. Start the project

```bash
python manage.py runserver
```
The app will run on your (localhost:8000)

## Lessons Learned

What did you learn while building this project?

✅ Different Class-Based Views.

✅ How they are implemented?

✅ Working behind the Class-Based Views.

    
## LICENSE

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/zengboi/CLI-Login-System/blob/main/LICENSE)

Copyright 2021 Mithilesh Gautam

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
# spr cs3980 assignment 1

```bash
python3 -m venv venv
source ../.venv/bin/activate  or  . venv/bin/activate
pip3 install fastapi
pip3 install uvicorn
pip3 install functools
pip3 install matplotlib
```

Create a python file 'api.py' with code.

```bash
uvicorn api:app --reload
```

After everything is looking good, make a requirements.txt file before committing
```bash
pip3 freeze > requirements.txt
```
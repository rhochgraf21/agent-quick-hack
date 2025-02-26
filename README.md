# agent-quick-hack

Let's try to build an agent in an hour. Can it be done?

[Read the PDF](agent-quick-hack-introduction.pdf)

[How to contribute](CONTRIBUTING.md)

## Instructions

Install requirements

```bash
pip install -r requirements.txt
```

Generate the SQL databases

```bash
python dataset_to_sqlite.py
```


## Running the Flask Server:

```
pip install -r requirements.txt  # install python dependencies 
cd src                           # navigate to the src directory
python main.py                   # run the Flask server
```
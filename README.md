# flasklite

flasklite is meant to provide a simple structure for Flask projects.

## How to Run
> 1. Clone repository: <code>git clone https://www.github.com/sampson-q/flasklite</code>
> 2. Change into the cloned directory
> 3. Run setup.py: <code>python setup.py install</code>
> 4. run flasklite (with options)<br>
>> <pre>
>> Usage: flasklite [options], flasklite -p projectname
>> 
>> options:             description:
>> -h, --help           display help of this command
>> -p [projectname]     creates a new project
>> </pre>

## Intended Structure
<pre>
projectname\
|__ projectnameApp\
|   |__ static\
|   |__ templates\
|      |__ base.html
|   |__ __init__.py
|   |__ auth.py
|   |__ views.py
|__  main.py
</pre>
## Requirements
> 1. Python 3 (must be added to path)
> 2. Flask
> 3. Flask-Login
> 4. pip

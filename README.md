# Learning Python API using Flask

On this example I am creating a simple api using Flask, 
to create / update and delete tasks, the data will be persisted on JSON file. 

## Get task by ID:
- http://127.0.0.1:5000/tasks?id=0

## Add new task 
```bash  
    curl --location --request PUT 'http://127.0.0.1:5000/tasks?id=1' \
        --header 'Content-Type: application/json' \
        --data '{
                "title": "bla",
                "description": "bla-blup"
            }'
```

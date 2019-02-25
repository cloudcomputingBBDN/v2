1)To add category:

curl -i -H "Content-Type: application/json" -X POST -d '["eeee"]' http://localhost:5000/api/v1/categories





2)To delete a category:

curl -X DELETE http://localhost:5000/CC/A2/Categories/del/c




3) To add a user

curl -i -H "Content-Type: application/json" -X POST -d '{"name":"foodeaer","pass":"d307c260590934729aee431950af672bdbda16ab"}' http://localhost:5000/api/v1/users



4) to delete a user

curl -X DELETE http://localhost:5000/api/v1/users/foodeater


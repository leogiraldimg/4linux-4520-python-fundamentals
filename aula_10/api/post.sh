curl -d \
'{"mensagem": "'$1'"}' \
-H "Content-Type: application/json" \
--request POST \
http://localhost:5000/post

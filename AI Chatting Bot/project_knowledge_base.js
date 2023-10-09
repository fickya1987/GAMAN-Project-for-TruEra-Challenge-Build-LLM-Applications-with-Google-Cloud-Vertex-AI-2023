# https://developer.voiceflow.com/reference/post_knowledge-base-query
API_KEY='{api_key}'

QUESTION='why is the sky blue?'

curl --request POST 'https://general-runtime.voiceflow.com/knowledge-base/query' \
     --header "Authorization: $API_KEY" \
     --header 'Accept: application/json' \
     --header 'Content-Type: application/json' \
     --data "{
      \"question\": \"$QUESTION\"
     }"

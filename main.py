import requests
from collections import Counter

def get_total_scores(user, score_map):
  ENDPOINT = 'https://api.github.com/users/{}/events'.format(user)
  payload = requests.get(ENDPOINT).json()
  total_score = 0
  list_of_events = [event['type'] for event in payload]
  c = Counter(list_of_events)
  for key in c:
    if key in score_map:
      score = score_map[key] * c[key]
      total_score += score
    else:
      total_score += c[key]
  return total_score
  
score_map = {
    'PullRequestEvent':5,
    'ForkEvent':4, 
    'IssueCommentEvent':3,
    'PushEvent':2,
    'other':1
}
print(get_total_scores('danielspofford', score_map))
# making sure i push all my repls
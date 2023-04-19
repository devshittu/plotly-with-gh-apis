from operator import itemgetter
import json
import requests
import plotly.express as px

url="https://hacker-news.firebaseio.com/v0/topstories.json"
r=requests.get(url, timeout=3600)
print(f"Status code: {r.status_code}")

submission_ids = r.json()
submission_dicts = []

for submission_id in submission_ids[:5]:
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url, timeout=3600)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()
    # Build a dict for each article
    submission_dict = {
        'title': response_dict["title"],
        'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict["descendants"],
    }
    submission_dicts.append(submission_dict)
    
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)
submission_comment_counts, submission_links = [], [] 
for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")
    submission_comment_counts.append(submission_dict['comments'])
    submission_links.append(submission_dict['title'])
    
response_string = json.dumps(submission_dicts, indent=4)
print(response_string)

labels =  {'y': 'Comments', 'x': 'Aritcles'}
fig = px.bar(y=submission_comment_counts, x=submission_links, labels=labels)
# fig = px.pie(y=submission_comment_counts, x=submission_links, labels=labels)
df = px.data.tips()
fig = px.pie(df, values=submission_comment_counts, names=submission_links)
# fig.update_layout()
fig.show()

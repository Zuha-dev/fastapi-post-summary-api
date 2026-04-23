import re


def search_and_summarize(data,user_id, keyword=None, min_length=None):

    if keyword is not None:
        keyword = keyword.lower()

    filtered = []

    for post in data:
        if user_id != post['userId']:
            continue
        if keyword is not None:
            clean = re.sub(r'[^a-zA-Z0-9\s]', '', post['body'])
            words = clean.lower().split()
            if keyword.lower() not in words:
                continue 
        if min_length is not None and len(post['body']) < min_length:
            continue
        filtered.append(post)

    if not filtered:
        return {
            "user_id": user_id,
            "total_posts":0,
            "average_length":0,
            "longest_post":None
        }
    
    total_results = len(filtered)
    total_length = sum(len(p["body"]) for p in filtered)   
    average_length = total_length / total_results
    longest_post = max(filtered, key=lambda post:len(post['body']))

    return {
        "user_id": user_id,
        "total_posts": total_results,
        "average_length": round(average_length, 2),
        "longest_post": {
            "id":longest_post['id'], 
            "length":len(longest_post['body']) 
            }
        }
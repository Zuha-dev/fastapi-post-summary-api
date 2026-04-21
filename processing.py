import re

def search_and_summarize(data, keyword=None, min_length=None):

    summary = {"total_results":0,
               "average_length":0,
               "longest_post":None}
    
    result = []
    
    for post in data:
        if keyword is not None:
            clean = re.sub(r'[^a-zA-Z0-9\s]', '', post['body'])
            words = clean.lower().split()
            if keyword.lower() not in words:
                continue
        if min_length is not None and  len(post['body']) < min_length:
            continue
        result.append(post)

    if result:
        total_results = len(result)

        total_body_length = 0     # later sum() could be done 
        for post in result:
            total_body_length += len(post['body'])

        avg_length = total_body_length /  total_results
        longest = max(result , key=lambda x:len(x ['body'])) 

    else:
        total_results = 0
        longest = None
        avg_length = 0

    summary["longest_post"]  = longest 
    summary["total_results"] = total_results
    summary["average_length"] = avg_length

    return summary


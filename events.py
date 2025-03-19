def handle_push(event, repo_name):
    commits = len(event["payload"]["commits"])
    print(f"> Pushed {commits} commits to {repo_name}")

def handle_pull_request(event, repo_name):
    action = event["payload"]["action"]
    pr_title = event["payload"]["pull_request"]["title"]
    print(f"> PR {action}: {pr_title} in {repo_name}")

def handle_issues(event, repo_name):
    action = event["payload"]["action"]
    issue_title = event["payload"]["issue"]["title"]
    print(f"> Issue {action}: {issue_title} in {repo_name}")

def handle_create(event, repo_name):
    ref_type = event["payload"]["ref_type"]
    print(f"> Created a new {ref_type} in {repo_name}")

def handle_fork(event, repo_name):
    print(f"> Forked {repo_name}")

def handle_watch(event, repo_name):
    action = event["payload"]["action"]
    print(f"> {repo_name} was {action}d by you")

def handle_commit_comment(event, repo_name):
    comment = event["payload"]["comment"]["body"]
    print(f"> Commented on a commit in {repo_name}: {comment}")

def handle_unknown(event, repo_name):
    event_type = event["type"]
    print(f"> Event of type {event_type} occurred in {repo_name}")

EVENT_HANDLERS = {
    "PushEvent": handle_push,
    "PullRequestEvent": handle_pull_request,
    "IssuesEvent": handle_issues,
    "CreateEvent": handle_create,
    "ForkEvent": handle_fork,
    "WatchEvent": handle_watch,
    "CommitCommentEvent": handle_commit_comment,
}
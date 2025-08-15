from datetime import date, datetime

def get_commits_by_date(
                        author_email: str, 
                        start_date: str, 
                        end_date: str, 
                        repo_name: str, 
                        repo_owner: str, 
                        branch: str):
    
    # Return a clean string without escaped characters
    return f"""query {{
        repository(owner: "{repo_owner}", name: "{repo_name}") {{
            ref(qualifiedName: "refs/heads/{branch}") {{
                target {{
                    ... on Commit {{
                        history(
                            since: "{start_date}T00:00:00Z"
                            until: "{end_date}T23:59:59Z"
                            first: 100
                            author: {{ emails: ["{author_email}"] }}
                        ) {{
                            pageInfo {{ hasNextPage endCursor }}
                            nodes {{
                                oid
                                committedDate
                                messageHeadline
                                additions
                                deletions
                                changedFiles
                                url
                                author {{ user {{ login }} email name }}
                            }}
                        }}
                    }}
                }}
            }}
        }}
    }}"""
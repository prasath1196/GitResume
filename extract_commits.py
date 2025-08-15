import re
from git import Repo
import json
import os
from os import path, makedirs
from src.commits.service import CommitService 



# def extract_commits():
#     repo = Repo.clone_from('https://github.com/prasath1196/human-essentials', 'tmp/human-essentials')

#     if repo.bare:
#         print("Repository is bare")
#     else:
#         print("Repository is not bare")


#     commits = repo.iter_commits() 

#     my_last_10_changes = []
#     for commit in list(commits)[:1000]:
#         author = commit.author
#         if re.search(r'prasath', author.name, re.IGNORECASE):   
#             print(f"Commit: {commit.hexsha[:8]}")
#             print(f"Author: {author.name}")
#             print(f"Date: {commit.committed_datetime}")
#             print(f"Message: {commit.message}")
#             my_last_10_changes.append({
#                 "commit": commit.hexsha[:8],
#                 "author": author.name,
#                 "date": commit.committed_datetime,
#                 "message": commit.message,
#                 "changes": []
#             })
#             # Get the diff for this commit
#             if commit.parents:
#                 # Compare with parent commit
#                 diff = commit.diff(commit.parents[0])
#                 print(f"Changes ({len(diff)} files):")
#                 for change in diff:
#                     if change.change_type == 'M':  # Modified
#                         print(f"  Modified: {change.a_path}")
#                         # Get full content before and after
#                         try:
#                             old_content = change.b_blob.data_stream.read().decode('utf-8') if change.b_blob else "File didn't exist"
#                             new_content = change.a_blob.data_stream.read().decode('utf-8') if change.a_blob else "File doesn't exist"
#                             print(f"    OLD CONTENT:\n{old_content}")
#                             print(f"    NEW CONTENT:\n{new_content}")
#                             my_last_10_changes[-1]["changes"].append({
#                                 "path": change.a_path,
#                                 "content": new_content
#                             })
#                         except Exception as e:
#                             print(f"    Error reading file content: {e}")
                            
#                     elif change.change_type == 'A':  # Added
#                         print(f"  Added: {change.a_path}")
#                         # Get full content of new file
#                         try:
#                             new_content = change.a_blob.data_stream.read().decode('utf-8')
#                             print(f"    FULL NEW FILE CONTENT:\n{new_content}")
#                             my_last_10_changes[-1]["changes"].append({
#                                 "path": change.a_path,
#                                 "content": new_content
#                             })
#                         except Exception as e:
#                             print(f"    Error reading file content: {e}")
                            
#                     elif change.change_type == 'D':  # Deleted
#                         print(f"  Deleted: {change.b_path}")
#                         # Get full content of deleted file
#                         try:
#                             old_content = change.b_blob.data_stream.read().decode('utf-8')
#                             print(f"    FULL DELETED FILE CONTENT:\n{old_content}")
#                             my_last_10_changes[-1]["changes"].append({
#                                 "path": change.b_path,
#                                 "content": old_content
#                             })
#                         except Exception as e:
#                             print(f"    Error reading file content: {e}")
                            
#                     elif change.change_type == 'R':  # Renamed
#                         print(f"  Renamed: {change.b_path} -> {change.a_path}")
#                         # Get content of both files
#                         try:
#                             old_content = change.b_blob.data_stream.read().decode('utf-8') if change.b_blob else "File didn't exist"
#                             new_content = change.a_blob.data_stream.read().decode('utf-8') if change.a_blob else "File doesn't exist"
#                             print(f"    OLD FILE ({change.b_path}):\n{old_content}")
#                             print(f"    NEW FILE ({change.a_path}):\n{new_content}")
#                             my_last_10_changes[-1]["changes"].append({
#                                 "path": change.a_path,
#                                 "content": new_content
#                             })
#                         except Exception as e:
#                             print(f"    Error reading file content: {e}")
                    
#                     print("    " + "-" * 50)
#             else:
#                 print("Initial commit - no parent to compare with")
            
#             print("--------------------------------")

#     # Write the changes to a JSON file
#     with open('my_last_10_changes.json', 'w', encoding='utf-8') as f:
#         json.dump(my_last_10_changes, f, indent=4, default=str)

#     os.rmdir('tmp/FinePrint-AI')


def extract_commits_api():
    repo = "FinePrint-AI" 
    author_email = "prasath1196@gmail.com" 
    start_date = "2025-01-01"
    end_date = "2025-12-31"
    branch = "main"
    owner = "prasath1196"
    commit_service = CommitService(repo, owner, author_email, start_date, end_date, branch)
    commits = commit_service.get_commits_by_date()
    print(commits)
if __name__ == "__main__":
    # extract_commits()
    extract_commits_api()
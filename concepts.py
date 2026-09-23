# Concepts Notebook

### 1. Git Staging Area
- **Definition:** A temporary preparation zone for files before saving a snapshot.
- **Why it exists:** Allows selecting exactly which files and changes to include in the next commit.

### 2. Git Branch
- **Definition:** An independent timeline or line of development separate from main.
- **Why it exists:** Enables working on new features safely without breaking the main codebase.

### 3. Pull Request (PR)
- **Definition:** A formal request to merge changes from one branch into another.
- **Why it exists:** Allows code review, discussion, and testing before code is merged into main.

### 4. .gitignore
- **Definition:** To make Git ignore a file in a folder that already contains Git.
- **Why it exists:** To help the users to upload folders to Git without the files they dont want to share with everyone like a file that contains passwords.

### 5. git diff
- **Definition:** Shows the exact line-by-line differences between your current code and the last saved state before staging.
- **Why it exists:** Allows developers to review their local changes carefully before running `git add` to prevent committing unintended bugs or temporary code.

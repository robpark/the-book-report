---
permissions: ["all"]
---

# Commit --> Push

Linting

* Ensure ruff check passes

Format a commit and get the appropriate confirmations through to git push.

* author a commit message
* stage all edited files
* **STOP AND WAIT FOR CONFIRMATION TO PROCEED**
* commit (pre-commit hooks will run: terraform fmt, tflint, tfsec)
* **STOP AND WAIT FOR CONFIRMATION TO PROCEED WITH PUSH**

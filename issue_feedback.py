from pathlib import Path
import subprocess
import sys

title, body, issue_number = sys.argv[-3:]


prompt = (
    Path("prompt.txt")
    .read_text()
    .replace("{{{ISSUE_TITLE}}}", title)
    .replace("{{{ISSUE_BODY}}}", body)
)


response = subprocess.check_output(["gh", "models", "run", "gpt-40-mini", prompt])


subprocess.check_call(
    ["gh", "issue", "comment", issue_number, "--body", response.decode("utf-8")]
)

from pathlib import Path
import subprocess
import sys

title, body, issue_number = sys.argv[-3:]


HEADER = """
🤖: Hi!  I'm a friendly robot here to give you advice on writing a better bug
report that our developers can more quickly and effectively act on.

"""


prompt = (
    Path("prompt.txt")
    .read_text()
    .replace("{{{ISSUE_TITLE}}}", title)
    .replace("{{{ISSUE_BODY}}}", body)
)


response = subprocess.check_output(["gh", "models", "run", "gpt-4o-mini", prompt])


response = HEADER + response.decode("utf-8")


subprocess.check_call(
    ["gh", "issue", "comment", issue_number, "--body", response.decode("utf-8")]
)

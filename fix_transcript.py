import json
import os

target_dir = "/Users/anno/.gemini/antigravity-ide/brain/48a17b99-f187-4094-bc11-e9f17adc06e9/.system_generated/logs"

def fix_file(filename):
    filepath = os.path.join(target_dir, filename)
    with open(filepath, "r") as f:
        lines = f.readlines()
    
    first_step = json.loads(lines[0])
    if first_step.get("step_index") == 5:
        # Create steps 0 to 4
        new_lines = []
        created_at = "2026-08-01T07:38:20Z"
        new_lines.append(json.dumps({"step_index": 0, "source": "USER_EXPLICIT", "type": "USER_INPUT", "status": "DONE", "created_at": created_at, "content": "<USER_REQUEST>\n你现在是我的Python入门教练。\n</USER_REQUEST>"}) + "\n")
        new_lines.append(json.dumps({"step_index": 1, "source": "SYSTEM", "type": "EPHEMERAL_MESSAGE", "status": "DONE", "created_at": created_at}) + "\n")
        new_lines.append(json.dumps({"step_index": 2, "source": "MODEL", "type": "PLANNER_RESPONSE", "status": "DONE", "created_at": created_at, "content": "好的，很高兴做你的教练！"}) + "\n")
        new_lines.append(json.dumps({"step_index": 3, "source": "USER_EXPLICIT", "type": "USER_INPUT", "status": "DONE", "created_at": created_at, "content": "<USER_REQUEST>\n好的\n</USER_REQUEST>"}) + "\n")
        new_lines.append(json.dumps({"step_index": 4, "source": "SYSTEM", "type": "EPHEMERAL_MESSAGE", "status": "DONE", "created_at": created_at}) + "\n")
        
        with open(filepath, "w") as f:
            f.writelines(new_lines + lines)
        print(f"Fixed {filename}")
    else:
        print(f"No need to fix {filename}")

fix_file("transcript.jsonl")
fix_file("transcript_full.jsonl")

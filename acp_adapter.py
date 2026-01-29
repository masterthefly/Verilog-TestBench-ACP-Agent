import json
import sys
import requests

ANTIGRAVITY_AGENT_URL = "http://localhost:8000/agent"  # adjust if needed

def send_to_agent(payload):
    try:
        r = requests.post(ANTIGRAVITY_AGENT_URL, json=payload)
        return r.json()
    except Exception as e:
        return {"error": str(e)}

def handle_acp_request(request):
    method = request.get("method")
    params = request.get("params", {})

    agent_payload = {
        "acp_method": method,
        "acp_params": params
    }

    agent_response = send_to_agent(agent_payload)
    return agent_response

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        request = json.loads(line)
        response = handle_acp_request(request)
        sys.stdout.write(json.dumps(response) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
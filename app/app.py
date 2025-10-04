from flask import Flask, jsonify
import requests

app = Flask(__name__)

base_github_api_url = "https://api.github.com"

@app.route("/<username>", methods=["GET"])
def fetch_user_gists(username):
    github_url = base_github_api_url + "/users/" + username + "/gists"
    try:
        res = requests.get(github_url)

        if res.status_code != 200:
            return_content = {
                "status": "error",
                "status_code": res.status_code,
                "message": res.json()["message"] or "User not found or GitHub API error",
                "error": "User not found or GitHub API error"
            }
            return jsonify(return_content), res.status_code

        res_data = res.json()

        gist_list = []

        for data in res_data:
            gist = {
                "id": data["id"],
                "url": data["html_url"],
                "description": data["description"] or "No description",
                "files": list(data["files"].keys()),
                "total_files": len(data["files"]),
                "created_at": data["created_at"],
                "updated_at": data["updated_at"]
            }
            gist_list.append(gist)

        return jsonify(gist_list)
    except Exception as e:
        return jsonify({"error": "Internal server error", "details": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

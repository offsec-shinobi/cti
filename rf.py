import requests
import json

def get_and_parse(url):
    
    try:
        response = requests.get(url)
        response.raise_for_status() 
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"JSON parsing error: {e}")
        return None


if __name__ == "__main__":
    # Example usage
    url = "https://api.ransomfeed.it"
    result = get_and_parse(url)
    
    if result:
        #print(json.dumps(result, indent=2))
        print(type(result))
    for i in result:
        print(i['hash'])
